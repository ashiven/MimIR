#include "mim/world.h"

#include "mim/plug/rise/rise.h"

namespace mim::plug::rise {

const Def* normalize_const(const Def* type, const Def*, const Def* arg) {
    auto& world = type->world();
    return world.lit(world.type_idx(arg), 42);
}

MIM_rise_NORMALIZER_IMPL

} // namespace mim::plug::rise
