// Created by Crowbar 0.67

$ModelName "spectrobes/shakoblade.mdl"

$BodyGroup "studio"
{
	studio "shakoblade.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition -0.007 -0.17 0.411

$CDMaterials "spectrobes\shakoblade\"

$CBox 0 0 0 0 0 0

$BBox -2.381 -1.349 -0.017 2.721 1.336 0.84


$Sequence "REF" {
	"shakoblade_anims\REF.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
