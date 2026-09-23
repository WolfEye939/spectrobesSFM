$ModelName "spectrobes/creatures/Komadoros.mdl"
$CDMaterials "models\spectrobes\creatures\Komadoros\"

$scale 3.0

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

