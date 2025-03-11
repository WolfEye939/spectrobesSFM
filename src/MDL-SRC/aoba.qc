// Created by Crowbar 0.67

$ModelName "spectrobes/Aoba.mdl"

$BodyGroup "studio"
{
	studio "Aoba.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 0 -0.982 16.838

$CDMaterials "spectrobes\Aoba\"

$CBox 0 0 0 0 0 0

$BBox -48.694 -77.047 -0.374 50.657 77.048 34.05


$Sequence "idle" {
	"aoba_anims\idle.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
