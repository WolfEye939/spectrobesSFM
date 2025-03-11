#model_name=spikan_GameModel
#created with IK-Rigger v1.2
#BY http://steamcommunity.com/id/OMGTheresABearInMyOatmeal/
#This is just a modified version of valves' biped simple script.
ik_1= [u'j_hiza_R', u'j_hiza_L', u'j_mune_B', u'j_mune_B']
ik_2= [u'e_ashi_R', u'e_ashi_L', u'j_sako_L', u'j_sako_R']
ik_3= [u'c_ashi_R', u'c_ashi_L', u'j_kata_L', u'j_kata_R']
ik_elbow_name= [u'FootR2', u'FootL2', u'CollarL', u'CollarR']
ik_hand_name= [u'footR', u'foot', u'ArmL', u'ArmR']
ik_spinelist= [u'j_mune_A', u'j_mune_B']
rig_to_rig_parent= {}
bone_to_rig_parent= {}
rig_name_to_bone= {}
axis_offset=[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]







import random,ast
import vs


#==================================================================================================
def AddValidObjectToList( objectList, obj ):
    if ( obj != None ): objectList.append( obj )
    
def invert_dict(d):
    return dict([(v, k) for k, v in d.iteritems()])




#==================================================================================================
def get_childeren(rig_name):
    temp=[]

    
    for elm in bone_to_rig_parent:
        
        if bone_to_rig_parent[elm]==rig_name:
            temp.append(elm)
            temp.extend(get_childeren( invert_dict(rig_name_to_bone)[elm]))
    return temp

    

#==================================================================================================
#gets string list of bone's rig name
def bone_to_rigname(bone_list):
    temp=[]
    tempdic=invert_dict(rig_name_to_bone)
    for elm in bone_list:
        temp.append(tempdic[elm])

    return temp

def get_list_of_fingers():
    fingers=[]
    for key in bone_to_rig_parent.keys():
        if  bone_to_rig_parent[key] in ik_hand_name:
            fingers.append(key)
            fingers.extend(get_childeren( invert_dict(rig_name_to_bone)[key]))

            

            
    return bone_to_rigname(fingers)

def CreateOrientConstraint( target, slave, bCreateControls=True, group=None ) :
    ''' Method for creating a single target orient constraint '''
    
    if ( target == None ):
        return

    targetDag = sfmUtils.GetDagFromNameOrObject( target )
    slaveDag = sfmUtils.GetDagFromNameOrObject( slave )
    
    sfm.PushSelection()
    sfmUtils.SelectDagList( [ targetDag, slaveDag ] )
    
    
    orientConstraintTarget = sfm.OrientConstraint( controls=bCreateControls )
    
    if ( group != None ):

        if ( orientConstraintTarget != None ):
            orientWeightControl = orientConstraintTarget.FindWeightControl()
            if ( orientWeightControl != None ):
                group.AddControl( orientWeightControl )
            
    sfm.PopSelection()
    return
#==================================================================================================
def HideControlGroups( rig, rootGroup, *groupNames ):
    for name in groupNames:    
        group = rootGroup.FindChildByName( name, False )
        if ( group != None ):
            rig.HideControlGroup( group )

    

#==================================================================================================
# Compute the direction from boneA to boneB
#==================================================================================================
def ComputeVectorBetweenBones( boneA, boneB, scaleFactor ):
    
    vPosA = vs.Vector( 0, 0, 0 )
    boneA.GetAbsPosition( vPosA )
    
    vPosB = vs.Vector( 0, 0, 0 )
    boneB.GetAbsPosition( vPosB )
    
    vDir = vs.Vector( 0, 0, 0 )
    vs.mathlib.VectorSubtract( vPosB, vPosA, vDir )
    vDir.NormalizeInPlace()
    
    vScaledDir = vs.Vector( 0, 0, 0 )
    vs.mathlib.VectorScale( vDir, scaleFactor, vScaledDir )    
    
    return vScaledDir
    
   
#==================================================================================================
# Build a simple ik rig for the currently selected animation set
#==================================================================================================
def BuildRig(helpoption):
    
    # Get the currently selected animation set and shot
    shot = sfm.GetCurrentShot()
    animSet = sfm.GetCurrentAnimationSet()
    gameModel = animSet.gameModel
    rootGroup = animSet.GetRootControlGroup()
    
    # Start the biped rig to which all of the controls and constraints will be added
    rig = sfm.BeginRig( "rig_biped_" + animSet.GetName()+str(random.randint(1,500)) );
    if ( rig == None ):
        return
    
    # Change the operation mode to passthrough so changes chan be made temporarily
    sfm.SetOperationMode( "Pass" )
    
    # Move everything into the reference pose
    sfm.SelectAll()
    sfm.SetReferencePose()
    
    #==============================================================================================
    # Find the dag nodes for all of the bones in the model which will be used by the script
    #==============================================================================================
    finger_group=get_list_of_fingers()
    boneRoot      = sfmUtils.FindFirstDag( [ "RootTransform" ], True )




    boneupper=[]
    ##[handlename:bone]
    boneelbow=[]
    bonehand=[]
    for i in range(len(ik_1)):

        
        boneupper.append(sfmUtils.FindFirstDag( [ ik_1[i] ], True ))
        boneelbow.append(sfmUtils.FindFirstDag( [ ik_2[i] ], True ))
        bonehand.append(sfmUtils.FindFirstDag( [ ik_3[i] ], True ))


    bone_spine=[]
    for i in range(len(ik_spinelist)):
        bone_spine.append(sfmUtils.FindFirstDag( [ ik_spinelist[i] ], True ))
        

           




##replace bone name string key with sfm bone obj
    for bone in bone_to_rig_parent.keys():
        temp=sfmUtils.FindFirstDag( [ bone ], True )
        bone_to_rig_parent[temp]=bone_to_rig_parent.pop(bone)
        
        for key in rig_name_to_bone.keys():
            if rig_name_to_bone[key] == bone:
                rig_name_to_bone[key]=temp



    #==============================================================================================
    # Create the rig handles and constrain them to existing bones
    #==============================================================================================
    rigRoot    = sfmUtils.CreateConstrainedHandle( "rig_root",     boneRoot,    bCreateControls=False )
 #maybe not needed   rig_bone["rigRoot"]=rigRoot
    
    for key in bone_to_rig_parent.keys():
  
        if bone_to_rig_parent[key] == "rigRoot":
            
            bone_to_rig_parent[key]=rigRoot
            
    for key in rig_to_rig_parent.keys():
  
        if rig_to_rig_parent[key] == "rigRoot":
            
            rig_to_rig_parent[key]=rigRoot
    
    rig_to_rig_Helper={}
    rig_hand=[]
    for i in range(len(ik_3)):
        rig_hand.append(sfmUtils.CreateConstrainedHandle( ik_hand_name[i],     bonehand[i],    bCreateControls=False ))
            # Create a helper handle which will remain constrained to the each foot position that can be used for parenting.
        temp= sfmUtils.CreateConstrainedHandle( ("rig_footHelper"+str(i)), bonehand[i], bCreateControls=False )
        rig_to_rig_Helper[rig_hand[-1]]=temp

        for key in bone_to_rig_parent.keys():
            if bone_to_rig_parent[key] == ik_hand_name[i]:
                bone_to_rig_parent[key]=rig_hand[-1]


        for key in rig_to_rig_parent.keys():
            if rig_to_rig_parent[key] == ik_hand_name[i]:
                rig_to_rig_parent[key]=rig_hand[-1]
            if key == ik_hand_name[i]:
                rig_to_rig_parent[rig_hand[-1]]=rig_to_rig_parent.pop(key)

                
    
    rig_spine=[]
    for i in range(len(bone_spine)):
        rig_spine.append(sfmUtils.CreateConstrainedHandle( "spine_"+str(i+1),     bone_spine[i],    bCreateControls=False ))
        
        a=("spine_"+str(i+1))

        for key in bone_to_rig_parent.keys():
            if bone_to_rig_parent[key] == a:
                bone_to_rig_parent[key]=rig_spine[-1]


        for key in rig_to_rig_parent.keys():
            if rig_to_rig_parent[key] == a:
                rig_to_rig_parent[key]=rig_spine[-1]
            if key == a:
                rig_to_rig_parent[rig_spine[-1]]=rig_to_rig_parent.pop(key)



        
 ######other            
              
    rig_bones=[]
    sfm_bones=[]
    bonerig_to_parent={}





#creates rigs thens copys the rig object to other dic that has it
##might need to optimize this part
    for key in rig_name_to_bone.keys():
        rig_bones.append(sfmUtils.CreateConstrainedHandle(key ,     rig_name_to_bone[key],    bCreateControls=False ))

        sfm_bones.append(rig_name_to_bone[key])

       # for x in bone_to_rig_parent.keys():
        if bone_to_rig_parent[rig_name_to_bone[key]]== key:
            print("yesssssss")
            bone_to_rig_parent[rig_name_to_bone[key]]=rig_bones[-1]

        for i in rig_to_rig_parent.keys():
            if rig_to_rig_parent[i] == key:
                rig_to_rig_parent[i]=rig_bones[-1]

        bonerig_to_parent[rig_bones[-1]]=bone_to_rig_parent[rig_name_to_bone[key]]

        
        
    for x in bonerig_to_parent.keys():
        if bonerig_to_parent[x] in rig_name_to_bone:  
            dex=sfm_bones.index(rig_name_to_bone[bonerig_to_parent[x]])
            bonerig_to_parent[x]=rig_bones[dex]



        
    
    # Use the direction from the heel to the toe to compute the knee offsets, 
    # this makes the knee offset indpendent of the inital orientation of the model.
    #vKneeOffsetR = ComputeVectorBetweenBones( boneFootR, boneToeR, 10 )
    #vKneeOffset = ComputeVectorBetweenBones( bonehand[0], bonehand[0], 10 )
    rig_elbows=[]
    
    
    for i in range(len(ik_2)):
        vKneeOffset = vs.Vector( axis_offset[i][0], axis_offset[i][1], axis_offset[i][2] )
        rig_elbows.append((sfmUtils.CreateOffsetHandle( ik_elbow_name[i], boneelbow[i], vKneeOffset,  bCreateControls=False )))
        
        for key in bone_to_rig_parent.keys():
            if bone_to_rig_parent[key] == ik_elbow_name[i]:
                bone_to_rig_parent[key]=rig_elbows[-1]
                
        for key in rig_to_rig_parent.keys():
            if rig_to_rig_parent[key] == ik_elbow_name[i]:
                rig_to_rig_parent[key]=rig_elbows[-1]
            if key == ik_elbow_name[i]:
                rig_to_rig_parent[rig_elbows[-1]]=rig_to_rig_parent.pop(key)












    # Create a list of all of the rig dags
    allRigHandles = [rigRoot]
    
    allRigHandles.extend(rig_hand+rig_elbows+rig_spine+rig_bones+rig_to_rig_Helper.keys())
    #==============================================================================================
    # Generate the world space logs for the rig handles and remove the constraints
    #==============================================================================================

    
    sfm.ClearSelection()
    sfmUtils.SelectDagList( allRigHandles )
    sfm.GenerateSamples()
    sfm.RemoveConstraints() 

    
    #==============================================================================================
    # Build the rig handle hierarchy
    #==============================================================================================
    #sfmUtils.ParentMaintainWorld( rigPelvis,        rigRoot )

    #for i in range(len (rig_hand)):
      #  sfmUtils.ParentMaintainWorld( rig_hand[i],        rigRoot )
    #    sfmUtils.ParentMaintainWorld( rig_elbows[i],        rig_hand[i] )
    


    for i in range(len(rig_spine)-1):
        sfmUtils.ParentMaintainWorld( rig_spine[i+1],        rig_spine[i] )




    for key in rig_to_rig_parent.keys():

        sfmUtils.ParentMaintainWorld( key,        rig_to_rig_parent[key] )
        
    for key in bonerig_to_parent.keys():

        if bonerig_to_parent[key]in rig_to_rig_Helper and  helpoption: #for bones parented to hands and foot i.e fingers,toes
            sfmUtils.ParentMaintainWorld( key,        rig_to_rig_Helper[bonerig_to_parent[key]] )
            continue

            
        sfmUtils.ParentMaintainWorld( key,        bonerig_to_parent[key] )
        




    # Set the defaults of the rig transforms to the current locations. Defaults are stored in local
    # space, so while the parent operation tries to preserve default values it is cleaner to just
    # set them once the final hierarchy is constructed.
    sfm.SetDefault()
    
    
    
    #==============================================================================================
    # Create constraints to drive the bone transforms using the rig handles
    #==============================================================================================
    
    # The following bones are simply constrained directly to a rig handle
    sfmUtils.CreatePointOrientConstraint( rigRoot,      boneRoot        )
    for i in range(len(rig_spine)):
        sfmUtils.CreatePointOrientConstraint( rig_spine[i],      bone_spine[i]        )


    i=0
    for key in rig_name_to_bone.keys():
        if key in finger_group:
            
            CreateOrientConstraint(rig_bones[i],      rig_name_to_bone[key]       )

        else:
          sfmUtils.CreatePointOrientConstraint(rig_bones[i],      rig_name_to_bone[key]       )  
        i+=1






    # Create ik constraints for the arms and legs that will control the rotation of the hip / knee and 
    # upper arm / elbow joints based on the position of the foot and hand respectively.

    for i in range(len(ik_1)):
        sfmUtils.BuildArmLeg( rig_elbows[i], rig_hand[i],      boneupper[i],  bonehand[i], True )
    



    
    #==============================================================================================
    # Create handles for the important attachment points 
    #==============================================================================================    
    attachmentGroup = rootGroup.CreateControlGroup( "Attachments" )  
    attachmentGroup.SetVisible( False )
    
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_heel_R",       attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_toe_R",        attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_outerFoot_R",  attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_innerFoot_R",  attachmentGroup )
    
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_heel_L",       attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_toe_L",        attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_outerFoot_L",  attachmentGroup )
    sfmUtils.CreateAttachmentHandleInGroup( "pvt_innerFoot_L",  attachmentGroup )
    

    HideControlGroups( rig, rootGroup, "Body", "Arms", "Legs", "Root" )
    rigBodyGroup = rootGroup.CreateControlGroup( "RigBody" )
    rigLimbsGroup = rootGroup.CreateControlGroup( "Limbs" )

    OtherGroup = rootGroup.CreateControlGroup( "Other Bones" )

    rigHelpersGroup = rootGroup.CreateControlGroup( "RigHelpers" )
    rigHelpersGroup.SetVisible( False )
    rigHelpersGroup.SetSnappable( False )

    for i in rig_spine:
        sfmUtils.AddDagControlsToGroup( rigBodyGroup, i  )

        
    sfmUtils.AddDagControlsToGroup( rigBodyGroup, rigRoot  )




    for i in rig_hand:
        sfmUtils.AddDagControlsToGroup( rigLimbsGroup,  i )

    for i in rig_elbows:
        sfmUtils.AddDagControlsToGroup( rigLimbsGroup,  i )



    for i in rig_bones:       
        sfmUtils.AddDagControlsToGroup( OtherGroup, i  )        

    for i in rig_to_rig_Helper.values():
        sfmUtils.AddDagControlsToGroup( rigHelpersGroup,i)
   # sfmUtils.MoveControlGroup( "rig_footRoll_L", rigLegsGroup, LeftLegGroup )
    #sfmUtils.MoveControlGroup( "rig_footRoll_R", rigLegsGroup, RightLegGroup )



    #sfmUtils.AddDagControlsToGroup( rigHelpersGroup, rigFootHelperR, rigFootHelperL )

    # Set the control group visiblity, this is done through the rig so it can track which
    # groups it hid, so they can be set back to being visible when the rig is detached.


    #Re-order the groups
    fingersGroup = rootGroup.FindChildByName( "Fingers", False )
    face = rootGroup.FindChildByName( "Face", False )
    rootGroup.MoveChildToBottom( face )
    rootGroup.MoveChildToBottom( rigBodyGroup )
    rootGroup.MoveChildToBottom( rigLimbsGroup )
    rootGroup.MoveChildToBottom( OtherGroup )
    

    other=rootGroup.FindChildByName( "Other", False )
    unknown=rootGroup.FindChildByName( "Unknown", False )
    
    rootGroup.MoveChildToBottom( fingersGroup )
    rootGroup.MoveChildToBottom( other )
    rootGroup.MoveChildToBottom( unknown )

    #==============================================================================================
    # Set the selection groups colors
    #==============================================================================================
    topLevelColor = vs.Color( 0, 128, 255, 255 )
    RightColor = vs.Color( 255, 0, 0, 255 )
    LeftColor = vs.Color( 0, 255, 0, 255 )

    rigBodyGroup.SetGroupColor( topLevelColor, False )
    rigLimbsGroup.SetGroupColor( topLevelColor, False )
    OtherGroup.SetGroupColor( topLevelColor, False )
    attachmentGroup.SetGroupColor( topLevelColor, False )
    


    
    # End the rig definition
    sfm.EndRig()
    return
    
#==================================================================================================
# Script entry
#==================================================================================================

# Construct the rig for the selected animation set
sfm.EndRig()

BuildRig(False);