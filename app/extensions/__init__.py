# https://www.pathofexile.com/item-filter/about

# Base class defining the common interface
from app.extensions.base_class import *

# Each rules block needs to start with Hide or Show
# TODO support "continue"
from app.extensions.show import *
from app.extensions.hide import *

# Basic extensions for matching the item
from app.extensions.area_level import *
from app.extensions.base_type import *
from app.extensions.base_defense_percentile import *
from app.extensions.class_name import *
from app.extensions.corrupt_implicit import *
from app.extensions.default_style import *
from app.extensions.elder import *
from app.extensions.fractured import *
from app.extensions.gem_level import *
from app.extensions.influenced import *
from app.extensions.item_level import *
from app.extensions.quality import *
from app.extensions.rarity import *
from app.extensions.socket_group import *
from app.extensions.sockets import *
from app.extensions.synthesised import *
from app.extensions.transfigured_gem import *
from app.extensions.veiled import *

# Basic extensions for modifying the style
from app.extensions.beam import *
from app.extensions.border import *
from app.extensions.font_size import *
from app.extensions.icon import *
from app.extensions.sound import *

# Complex extensions that combine multiple basic extensions
from app.extensions.tier_style import *
