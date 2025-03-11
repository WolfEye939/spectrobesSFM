// Created by Crowbar 0.67

$ModelName "spectrobes/Aoi.mdl"

$BodyGroup "studio"
{
	studio "aoi.smd"
}
$BodyGroup "blink"
{
	blank
	studio "aoi_Lids.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 0 -0.12 0.349

$CDMaterials "spectrobes\aoi\"

$CBox 0 0 0 0 0 0

$BBox -4.905 -6.99 -0.087 6.103 6.99 3.576


$Sequence "REF" {
	"aoi_anims\REF.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
