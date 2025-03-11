// Created by Crowbar 0.67

$ModelName "spectrobes/Leo.mdl"

$BodyGroup "studio"
{
	studio "Leo.smd"
}
$BodyGroup "Blink"
{
	blank
	studio "leo_Lids.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 0 -0.321 4.612

$CDMaterials "spectrobes\Leo\"

$TextureGroup "skinfamilies"
{
	{ "Leo2A" "Leo1A" }
	{ "Leo2B" "Leo1B" }
}

$CBox 0 0 0 0 0 0

$BBox -4.545 -2.069 -0.01 5.186 2.069 9.234


$Sequence "REF" {
	"leo_anims\REF.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
