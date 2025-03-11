// Created by Crowbar 0.67

$ModelName "spectrobes/Komainu.mdl"

$BodyGroup "studio"
{
	studio "Komainu.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 0 2.479 6.835

$CDMaterials "\spectrobes\Komainu\"

$TextureGroup "skinfamilies"
{
	{ "Komainu" }
	{ "Gold"    }
	{ "Silver"  }
}

$CBox 0 0 0 0 0 0

$BBox -10.833 -7.44 0 5.874 7.44 13.67


$Sequence "REF" {
	"komainu_anims\REF.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
