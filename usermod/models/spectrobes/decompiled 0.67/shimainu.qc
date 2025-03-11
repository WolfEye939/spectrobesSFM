// Created by Crowbar 0.67

$ModelName "spectrobes/Shimainu.mdl"

$BodyGroup "Studio"
{
	studio "Shimainu.smd"
}
$BodyGroup "Blink"
{
	blank
	studio "shimainu_Lids.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 0 -2.353 17.733

$CDMaterials "spectrobes\Shimainu\"

$CBox 0 0 0 0 0 0

$BBox -21.471 -16.746 0 26.178 16.746 35.466


$Sequence "REF" {
	"shimainu_anims\REF.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
