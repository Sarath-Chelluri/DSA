import os
import pathlib

already_deleted = os.listdir(
    "F:/Cartoonify Image/archive/face2comics_v2.0.0_by_Sxela/face2comics_v2.0.0_by_Sxela/faces"
)
to_delete = os.listdir(
    "F:/Cartoonify Image/archive/face2comics_v2.0.0_by_Sxela/face2comics_v2.0.0_by_Sxela/comics"
)

for j, i in enumerate(already_deleted):
    os.rename(
        src=f"F:/Cartoonify Image/archive/face2comics_v2.0.0_by_Sxela/face2comics_v2.0.0_by_Sxela/faces/{i}",
        dst=f"F:/Cartoonify Image/archive/face2comics_v2.0.0_by_Sxela/face2comics_v2.0.0_by_Sxela/faces/{str(j)}.jpeg",
    )
