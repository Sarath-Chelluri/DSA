import os
import pathlib

already_deleted = os.listdir(
    "F:/Cartoonify Image/archive/face2comics_v2.0.0_by_Sxela/face2comics_v2.0.0_by_Sxela/faces"
)
to_delete = os.listdir(
    "F:/Cartoonify Image/archive/face2comics_v2.0.0_by_Sxela/face2comics_v2.0.0_by_Sxela/comics"
)

for i in to_delete:
    if i not in already_deleted:
        file_to_rem = pathlib.Path(
            f"F:/Cartoonify Image/archive/face2comics_v2.0.0_by_Sxela/face2comics_v2.0.0_by_Sxela/comics/{i}"
        )
        file_to_rem.unlink()
