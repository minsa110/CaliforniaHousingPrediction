#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "AWS::s2n" for configuration "Release"
set_property(TARGET AWS::s2n APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(AWS::s2n PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libs2n.so"
  IMPORTED_SONAME_RELEASE "libs2n.so"
  )

list(APPEND _IMPORT_CHECK_TARGETS AWS::s2n )
list(APPEND _IMPORT_CHECK_FILES_FOR_AWS::s2n "${_IMPORT_PREFIX}/lib/libs2n.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
