#include "mim/plug/ll/ll.h"

#include <fstream>
#include <string>

#include <mim/config.h>

#include "mim/plugin.h"

#include "mim/util/sys.h"

namespace mim::ll {

using namespace std::string_literals;

void emit(World& world, std::ostream& ostream) {
    Emitter emitter(world, ostream);
    emitter.run();
}

int compile(World& world, std::string name) {
#ifdef _WIN32
    auto exe = name + ".exe"s;
#else
    auto exe = name;
#endif
    return compile(world, name + ".ll"s, exe);
}

int compile(World& world, std::string ll, std::string out) {
    std::ofstream ofs(ll);
    emit(world, ofs);
    ofs.close();
    auto cmd = std::format("clang \"{}\" -o \"{}\" -Wno-override-module", ll, out);
    return sys::system(cmd);
}

int compile_and_run(World& world, std::string name, std::string args) {
    if (compile(world, name) == 0) return sys::run(name, args);
    error("compilation failed");
}

} // namespace mim::ll

using namespace mim;

/// Backend entry point reached by the driver via `Driver::get_fun_ptr`.
extern "C" MIM_EXPORT void mim_emit_ll(World& world, std::ostream& ostream) { ll::emit(world, ostream); }

extern "C" MIM_EXPORT Plugin mim_get_plugin() { return {"ll", MIM_VERSION, nullptr, nullptr}; }
