# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.12

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/xenon/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/182.4505.18/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/xenon/.local/share/JetBrains/Toolbox/apps/CLion/ch-0/182.4505.18/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/Library_Management_System.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/Library_Management_System.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/Library_Management_System.dir/flags.make

CMakeFiles/Library_Management_System.dir/main.c.o: CMakeFiles/Library_Management_System.dir/flags.make
CMakeFiles/Library_Management_System.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/Library_Management_System.dir/main.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/Library_Management_System.dir/main.c.o   -c "/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System/main.c"

CMakeFiles/Library_Management_System.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/Library_Management_System.dir/main.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System/main.c" > CMakeFiles/Library_Management_System.dir/main.c.i

CMakeFiles/Library_Management_System.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/Library_Management_System.dir/main.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System/main.c" -o CMakeFiles/Library_Management_System.dir/main.c.s

# Object files for target Library_Management_System
Library_Management_System_OBJECTS = \
"CMakeFiles/Library_Management_System.dir/main.c.o"

# External object files for target Library_Management_System
Library_Management_System_EXTERNAL_OBJECTS =

Library_Management_System: CMakeFiles/Library_Management_System.dir/main.c.o
Library_Management_System: CMakeFiles/Library_Management_System.dir/build.make
Library_Management_System: CMakeFiles/Library_Management_System.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable Library_Management_System"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/Library_Management_System.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/Library_Management_System.dir/build: Library_Management_System

.PHONY : CMakeFiles/Library_Management_System.dir/build

CMakeFiles/Library_Management_System.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/Library_Management_System.dir/cmake_clean.cmake
.PHONY : CMakeFiles/Library_Management_System.dir/clean

CMakeFiles/Library_Management_System.dir/depend:
	cd "/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System" "/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System" "/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System/cmake-build-debug" "/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System/cmake-build-debug" "/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/21.09.2018/Library Management System/cmake-build-debug/CMakeFiles/Library_Management_System.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/Library_Management_System.dir/depend

