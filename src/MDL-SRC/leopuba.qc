// Created by Crowbar 0.67

$ModelName "spectrobes/Leopuba.mdl"

$BodyGroup "studio"
{
	studio "Leopuba.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 0 0.784 12.377

$CDMaterials "spectrobes\Leopuba\"

$TextureGroup "skinfamilies"
{
	{ "leopuba"     }
	{ "leopubaRare" }
}

$CBox 0 0 0 0 0 0

$BBox -17.749 -4.402 -0.031 16.181 4.402 24.786


$Sequence "REF" {
	"leopuba_anims\REF.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
