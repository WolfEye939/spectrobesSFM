// Created by Crowbar 0.67

$ModelName "spectrobes/Komanatos.mdl"

$BodyGroup "body"
{
	studio "Komanatos.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 0 -6.213 25.842

$CDMaterials "spectrobes\komanoto\"
$CDMaterials ""

$CBox 0 0 0 0 0 0

$BBox -25.602 -19.077 -0.623 38.028 19.077 52.307


$Sequence "idle" {
	"komanatos_anims\idle.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
