#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "AWS::aws-c-http" for configuration "Release"
set_property(TARGET AWS::aws-c-http APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(AWS::aws-c-http PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libaws-c-http.so.1.0.0"
  IMPORTED_SONAME_RELEASE "libaws-c-http.so.1.0.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS AWS::aws-c-http )
list(APPEND _IMPORT_CHECK_FILES_FOR_AWS::aws-c-http "${_IMPORT_PREFIX}/lib/libaws-c-http.so.1.0.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
