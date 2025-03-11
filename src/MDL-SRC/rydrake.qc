// Created by Crowbar 0.67

$ModelName "spectrobes/Rydrake.mdl"

$BodyGroup "studio"
{
	studio "Rydrake.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition -0.025 -3.733 12.895

$CDMaterials "spectrobes\Rydrake\"

$CBox 0 0 0 0 0 0

$BBox -12.965 -5.467 0 20.43 5.417 25.79


$Sequence "idle" {
	"rydrake_anims\idle.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
