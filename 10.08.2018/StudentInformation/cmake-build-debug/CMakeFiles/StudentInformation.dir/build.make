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
CMAKE_COMMAND = /home/xenon/CLion/clion-2018.2.1/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/xenon/CLion/clion-2018.2.1/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/StudentInformation.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/StudentInformation.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/StudentInformation.dir/flags.make

CMakeFiles/StudentInformation.dir/main.c.o: CMakeFiles/StudentInformation.dir/flags.make
CMakeFiles/StudentInformation.dir/main.c.o: ../main.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/StudentInformation.dir/main.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/StudentInformation.dir/main.c.o   -c /home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation/main.c

CMakeFiles/StudentInformation.dir/main.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/StudentInformation.dir/main.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation/main.c > CMakeFiles/StudentInformation.dir/main.c.i

CMakeFiles/StudentInformation.dir/main.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/StudentInformation.dir/main.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation/main.c -o CMakeFiles/StudentInformation.dir/main.c.s

# Object files for target StudentInformation
StudentInformation_OBJECTS = \
"CMakeFiles/StudentInformation.dir/main.c.o"

# External object files for target StudentInformation
StudentInformation_EXTERNAL_OBJECTS =

StudentInformation: CMakeFiles/StudentInformation.dir/main.c.o
StudentInformation: CMakeFiles/StudentInformation.dir/build.make
StudentInformation: CMakeFiles/StudentInformation.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable StudentInformation"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/StudentInformation.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/StudentInformation.dir/build: StudentInformation

.PHONY : CMakeFiles/StudentInformation.dir/build

CMakeFiles/StudentInformation.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/StudentInformation.dir/cmake_clean.cmake
.PHONY : CMakeFiles/StudentInformation.dir/clean

CMakeFiles/StudentInformation.dir/depend:
	cd /home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation /home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation /home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation/cmake-build-debug /home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation/cmake-build-debug /home/xenon/Xenon/Study_Stuffs/c/SoftwareEngineering/10.08.2018/StudentInformation/cmake-build-debug/CMakeFiles/StudentInformation.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/StudentInformation.dir/depend
