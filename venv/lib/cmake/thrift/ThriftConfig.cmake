#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

set(THRIFT_VERSION 0.15.0)


####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was ThriftConfig.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

macro(set_and_check _var _file)
  set(${_var} "${_file}")
  if(NOT EXISTS "${_file}")
    message(FATAL_ERROR "File or directory ${_file} referenced by variable ${_var} does not exist !")
  endif()
endmacro()

macro(check_required_components _NAME)
  foreach(comp ${${_NAME}_FIND_COMPONENTS})
    if(NOT ${_NAME}_${comp}_FOUND)
      if(${_NAME}_FIND_REQUIRED_${comp})
        set(${_NAME}_FOUND FALSE)
      endif()
    endif()
  endforeach()
endmacro()

####################################################################################

set_and_check(THRIFT_INCLUDE_DIR "/workspaces/CaliforniaHousingPrediction/venv/include/thrift")
set_and_check(THRIFT_CMAKE_DIR "/workspaces/CaliforniaHousingPrediction/venv/lib/cmake/thrift")
set_and_check(THRIFT_BIN_DIR "/workspaces/CaliforniaHousingPrediction/venv/bin")
set(THRIFT_COMPILER "${THRIFT_BIN_DIR}/thrift")

if (NOT TARGET thrift::thrift)
    include("${THRIFT_CMAKE_DIR}/thriftTargets.cmake")
endif()
set(THRIFT_LIBRARIES thrift::thrift)

if(TRUE AND ON)
    if (NOT TARGET thriftz::thriftz)
        include("${THRIFT_CMAKE_DIR}/thriftzTargets.cmake")
    endif()
    set(THRIFT_LIBRARIES thriftz::thriftz)
endif()

if ("${THRIFT_LIBRARIES}" STREQUAL "")
    message(FATAL_ERROR "thrift libraries were not found")
endif()
if (NOT Thrift_FIND_QUIETLY)
    message(STATUS "Found thrift: ${PACKAGE_PREFIX_DIR}")
endif()


include(CMakeFindDependencyMacro)

if(TRUE AND ON)
    find_dependency(ZLIB)
endif()

if(TRUE AND ON)
    find_dependency(OpenSSL)
endif()

if(TRUE AND ON)
    find_dependency(Libevent)
endif()

check_required_components(Thrift)
