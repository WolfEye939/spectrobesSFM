// Created by Crowbar 0.67

$ModelName "spectrobes/Spikanor.mdl"

$BodyGroup "studio"
{
	studio "Spikanor.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 0 -17.509 15.086

$CDMaterials "spectrobes\Spikanor\"

$TextureGroup "skinfamilies"
{
	{ "phong2" "phong3" "phong4" "phong1" }
	{ "phongB" "phongC" "phongD" "phongA" }
}

$CBox 0 0 0 0 0 0

$BBox -24.637 -25.994 -3.897 59.654 25.987 34.064


$Sequence "ref" {
	"spikanor_anims\ref.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
