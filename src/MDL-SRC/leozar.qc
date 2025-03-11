// Created by Crowbar 0.67

$ModelName "spectrobes/leozar.mdl"

$BodyGroup "studio"
{
	studio "Leozar.smd"
}


$SurfaceProp "default"

$Contents "solid"

$IllumPosition 17.513 0 23.745

$CDMaterials "spectrobes\leozar\"

$TextureGroup "skinfamilies"
{
	{ "Leozar"     }
	{ "leozarRare" }
}

$CBox 0 0 0 0 0 0

$BBox -21.479 -23.051 -0.027 21.479 58.077 47.517


$Sequence "REF" {
	"leozar_anims\REF.smd"
	fadein 0.2
	fadeout 0.2
	fps 30
}
