// Created by Crowbar 0.67

$ModelName "spectrobes/Ryza.mdl"

$BodyGroup "Studio"
{
	studio "Ryza.smd"
}
$BodyGroup "Blink"
{
	blank
	studio "ryza_Lids.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 0 -0.136 16.691

$CDMaterials "spectrobes\Ryza\"

$CBox 0 0 0 0 0 0

$BBox -15.998 -11.249 0 16.27 11.249 33.383


$Sequence "REF" {
	"ryza_anims\REF.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
