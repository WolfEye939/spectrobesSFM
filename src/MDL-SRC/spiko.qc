// Created by Crowbar 0.67

$ModelName "spectrobes/Spiko.mdl"

$BodyGroup "studio"
{
	studio "spiko.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 9.564 0.009 7.916

$CDMaterials "spectrobes\spiko\"

$CBox 0 0 0 0 0 0

$BBox -9.912 -14.429 -1.07 9.894 33.556 16.903


$Sequence "static" {
	"spiko_anims\static.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}

$Sequence "Idle" {
	"spiko_anims\Idle.smd"
	activity "ACT_IDLE" 1
	fadein 0.2
	fadeout 0.2
	fps 30
	loop
}
