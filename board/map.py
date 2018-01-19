

DIRT = "dirt"
GRAS = "grass"
MNTN = "mountain"

no_mtn_a  = [DIRT, DIRT, GRAS, GRAS, GRAS, DIRT, DIRT, DIRT, DIRT, DIRT]
no_mtn_b  = [DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRAS, GRAS, GRAS]
one_mtn = [DIRT, DIRT, DIRT, DIRT, DIRT, MNTN, DIRT, DIRT, DIRT, DIRT]

map_40x40 = [
    [one_mtn + one_mtn + one_mtn + one_mtn],
    [no_mtn_a + no_mtn_a + no_mtn_b + no_mtn_b],
    [no_mtn_a + no_mtn_b + no_mtn_a + no_mtn_b],
    [no_mtn_b + no_mtn_b + no_mtn_a + no_mtn_a],
]*4