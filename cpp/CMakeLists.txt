cmake_minimum_required(VERSION 3.14)
project(AtCoder)

set(CMAKE_CXX_STANDARD 14)

find_package(Boost 1.70.0 COMPONENTS system filesystem REQUIRED)
if(Boost_FOUND)
    message(STATUS "Boost_INCLUDE_DIRS: ${Boost_INCLUDE_DIRS}")
    message(STATUS "Boost_LIBRARIES: ${Boost_LIBRARIES}")
    message(STATUS "Boost_VERSION: ${Boost_VERSION}")
    include_directories(${Boost_INCLUDE_DIRS})
endif()

# 指定したとこ含めて、cppファイルがあったらビルド構成作る
MACRO(CREATE_BINARY target_dir)
    # 指定したディレクトリの中身一覧（孫までは取れない）
    FILE(GLOB children RELATIVE ${target_dir} ${target_dir}/*)
    FOREACH(child ${children})
        SET(path ${target_dir}/${child})
        # ディレクトリなら更に潜る、生成されるディレクトリは除外
        IF(IS_DIRECTORY ${path} AND NOT ${path} MATCHES "cmake-build-debug")
            CREATE_BINARY(${path})
        # cppファイルならバイナリー作成
        ELSEIF(${path} MATCHES \.cpp$)
            # バイナリー名を用意
            SET(binary_name "")
            STRING(REGEX MATCH [^\/]+\/[^\/]+\.cpp$ binary_name ${path})
            STRING(REGEX REPLACE "\/" "_" binary_name ${binary_name})
            STRING(REGEX REPLACE "\.cpp" "" binary_name ${binary_name})
            # 実行可能ファイルを追加
            ADD_EXECUTABLE(${binary_name} ${path})
        ENDIF()
    ENDFOREACH()
ENDMACRO()

CREATE_BINARY(${CMAKE_CURRENT_SOURCE_DIR})