// Created by Crowbar 0.67

$ModelName "spectrobes/creatures/Komadoros.mdl"
$CDMaterials "models\spectrobes\creatures\Komadoros\"

$body body "Komadoros_rework.dmx"

$sequence REF "Komadoros_rework.dmx"


// uses older model with split materials 
// above mesh uses less materials 
// so only 9 materials are called instead of 15.

// $body "body" "Komadoros.dmx"
// $sequence "idle" "Komadoros.dmx"


$texturegroup "skins" 
{
	{ Komadoros gold }
	{ Komadoros_GD gold_GD }
	{ Komadoros_SV gold_SV }
}

$SurfaceProp "default"
$Contents "solid"


$CBox 0 0 0 0 0 0
$BBox -9.017 -4.549 -0.12 8.869 4.55 9.796
$IllumPosition 0 0.074 4.838


