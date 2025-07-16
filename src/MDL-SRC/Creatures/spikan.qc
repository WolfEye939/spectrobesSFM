// Created by Crowbar 0.67

$ModelName "spectrobes/creatures/spikan.mdl"
$CDMaterials "models\spectrobes\creatures\spikan\"

$Body body "spikan.dmx"


$SurfaceProp "flesh"

$Contents "solid"

$IllumPosition 0 -14.271 12.389



// $Attachment "forward" "ValveBiped.forward" 0 0 0 rotate 0 0 0

$CBox 0 0 0 0 0 0

$BBox -26.414 -22.78 -3.659 36.311 22.781 24.779

//===============================
// Jigglebones are automatically 
// enforced and hidden when ragdoll 
// addons are used so this will be
// ignored for now
//===============================

/*
$JiggleBone "j_sippo_A"
{
	is_rigid
	{
		length 20
		tip_mass 100
		angle_constraint 60.000002
	}
}
$JiggleBone "j_sippo_B"
{
	is_rigid
	{
		length 20
		tip_mass 100
		angle_constraint 60.000002
	}
}
$JiggleBone "j_sippo_C"
{
	is_rigid
	{
		length 20
		tip_mass 100
		angle_constraint 60.000002
	}
}
$JiggleBone "j_sippo_D"
{
	is_rigid
	{
		length 20
		tip_mass 100
		angle_constraint 60.000002
	}
}
$JiggleBone "j_sippo_E"
{
	is_rigid
	{
		length 20
		tip_mass 100
		angle_constraint 60.000002
	}
}
$JiggleBone "j_sippo_F"
{
	is_rigid
	{
		length 20
		tip_mass 100
		angle_constraint 60.000002
	}
}
$JiggleBone "j_sippo_G"
{
	is_rigid
	{
		length 20
		tip_mass 100
		angle_constraint 60.000002
	}
}
$JiggleBone "j_sippo_H"
{
	is_rigid
	{
		length 20
		tip_mass 100
		angle_constraint 60.000002
	}
}
$JiggleBone "mane"
{
	is_rigid
	{
		length 20
		tip_mass 100
		angle_constraint 60.000002
	}
}
*/

// Dafuq is this?!!
// $SectionFrames 30 350

$sequence idle "Spikan.dmx"

/*
$Sequence "REF" {
	"spikan_anims\REF.smd"

}


$Sequence "idle" {
	"spikan_anims\idle.smd"

}


$Sequence "tailswing" {
	"spikan_anims\tailswing.smd"

	loop
}

$CollisionModel "spikan_physics.smd"
{
	$mass 1
	$inertia 1
	$damping 0
	$rotdamping 0
	$rootbone "j_sippo_a"
}
*/