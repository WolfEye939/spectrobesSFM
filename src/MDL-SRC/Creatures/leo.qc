// Created by Crowbar 0.67

$ModelName "spectrobes/creatures/Leo.mdl"

$body "body" "Leo.smd"


$BodyGroup "Blink"
{
	blank
	studio "leo_Lids.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 0 -0.321 4.612

$CDMaterials "models\spectrobes\creatures\Leo\"

$TextureGroup "skinfamilies"
{
	{ "Leo2A" "Leo1A" }
	{ "Leo2B" "Leo1B" }
}

$CBox 0 0 0 0 0 0

$BBox -4.545 -2.069 -0.01 5.186 2.069 9.234


$sequence "idle" "Leo.smd"
