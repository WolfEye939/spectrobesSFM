// Created by Crowbar 0.67

$ModelName "spectrobes/Hikolossa.mdl"

$BodyGroup "body"
{
	studio "hikolossa_body.smd"
}
$BodyGroup "rotors"
{
	studio "hikolossa_rotors.smd"
	blank
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 0 -4.105 9.474

$CDMaterials "spectrobes\Hikolossa\"

$CBox 0 0 0 0 0 0

$BBox -12.276 -21.268 -17.913 20.487 21.268 36.861


$Sequence "REF" {
	"hikolossa_anims\REF.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
