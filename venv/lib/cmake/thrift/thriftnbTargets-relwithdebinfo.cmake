#----------------------------------------------------------------
# Generated CMake target import file for configuration "RelWithDebInfo".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "thriftnb::thriftnb" for configuration "RelWithDebInfo"
set_property(TARGET thriftnb::thriftnb APPEND PROPERTY IMPORTED_CONFIGURATIONS RELWITHDEBINFO)
set_target_properties(thriftnb::thriftnb PROPERTIES
  IMPORTED_LOCATION_RELWITHDEBINFO "${_IMPORT_PREFIX}/lib/libthriftnb.so.0.15.0"
  IMPORTED_SONAME_RELWITHDEBINFO "libthriftnb.so.0.15.0"
  )

list(APPEND _IMPORT_CHECK_TARGETS thriftnb::thriftnb )
list(APPEND _IMPORT_CHECK_FILES_FOR_thriftnb::thriftnb "${_IMPORT_PREFIX}/lib/libthriftnb.so.0.15.0" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
