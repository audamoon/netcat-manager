from common.controllers import JSONController
from common.subdivion import SubdivisionController


js = JSONController()
c = SubdivisionController()


# c.write_subs_to_delete()

c.delete_subs(js,"temp/subdivision_to_delete.txt")
