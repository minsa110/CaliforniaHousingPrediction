#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "thriftz::thriftz" for configuration "RelWithDebInfo"
set_property(TARGET thriftz::thriftz APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(thriftz::thriftz PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libthriftz.so.0.15.0"
  IMPORTED_SONAME_RELWITHDEBINFO "libthriftz.so.0.15.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS thriftz::thriftz )
list(APPEND _IMPORT_CHECK_FILES_FOR_thriftz::thriftz "${_IMPORT_PREFIX}/lib/libthriftz.so.0.15.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
