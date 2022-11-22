#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "thrift::thrift" for configuration "RelWithDebInfo"
set_property(TARGET thrift::thrift APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(thrift::thrift PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libthrift.so.0.15.0"
  IMPORTED_SONAME_RELWITHDEBINFO "libthrift.so.0.15.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS thrift::thrift )
list(APPEND _IMPORT_CHECK_FILES_FOR_thrift::thrift "${_IMPORT_PREFIX}/lib/libthrift.so.0.15.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
