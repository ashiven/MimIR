.PHONY: build compile build-lit test

# NOTE: use flag "-G Ninja" to generate compile_commands.json on Windows
build:
	cmake -S . -B build \
		-DBUILD_TESTING=ON \
		-DMIM_BUILD_EXAMPLES=ON \
		-DCMAKE_EXPORT_COMPILE_COMMANDS=1 \
		-DCMAKE_INSTALL_PREFIX="C:\Users\janni\OneDrive\Dokumente\Projects\C++\MimIR\build\install"


compile:
	cmake --build build -j 8 --target install -- /verbosity:quiet

build-lit:
	cmake --build build -j 8 --target lit -- /verbosity:quiet

test:
	cd lit && ./lit ../build/lit/eqsat -a
