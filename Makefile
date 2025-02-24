.PHONY: build install test clean lint format

RELEASE_TYPE = Release
PY_SRC = src/pysrc
CPP_SRC = src/cppsrc

build: install
	cd build && cmake .. -DCMAKE_TOOLCHAIN_FILE=$(RELEASE_TYPE)/generators/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=$(RELEASE_TYPE) -G Ninja
	cd build && cmake --build .
	@cp -f build/*.so $(PY_SRC)

install_dependencies: 
	pipx install conan 
	conan profile detect
	python -m pip install --upgrade pip
	pipx install poetry

install:
	conan install . --build=missing
	poetry install

python_test: build
	@poetry run pytest $(PY_SRC)/test

cpp_test: build
	@cd build && ./intern_tests

clean:
	@rm -rf build
	@rm -f $(PY_SRC)/*.so

lint: pylint cpplint

pylint:
	poetry run mypy $(PY_SRC)
	poetry run ruff check $(PY_SRC)
	poetry run ruff format --check $(PY_SRC)

cpplint:
	find src -name '*.cpp' -o -name '*.hpp' | xargs clang-format --style=file --dry-run -Werror
	run-clang-tidy -j $(shell nproc) -p build

format:
	find $(CPP_SRC) -name '*.cpp' -o -name '*.hpp' | xargs clang-format -i
	poetry run ruff format $(PY_SRC)
	poetry run ruff check --fix $(PY_SRC)