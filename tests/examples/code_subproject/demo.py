from beet import Context, subproject


def beet_default(ctx: Context):
    ctx.require(subproject({"data_pack": {"load": ["src"]}}))
