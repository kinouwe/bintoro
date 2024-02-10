import maya.cmds as cmds


def select_inf_vertex():
    '''
    使い方: ジョイント（複数選択可）、メッシュ（最大1）を選択して実行
    機能：選択しているジョイントに関連するウェイトの頂点を頂点モードで選択する
    '''
    # 選択ノードを取得
    selection = cmds.ls(sl=True)

    if len(cmds.ls(sl=True, type='transform')) == 2:
        cmds.warning('メッシュが2つ以上選択されています。メッシュは1つだけ選択してください。')

    # 選択しているノードをメッシュとジョイントに振り分け
    mesh = []
    joints = []
    for sel in selection:
        if cmds.listRelatives(sel, type='mesh'):
            mesh.append(sel)
        elif cmds.ls(sel, type='joint'):
            joints.append(sel)

    sc = cmds.listConnections(f'{mesh[0]}.inMesh', d=True)

    # ウェイトの頂点選択
    cmds.skinCluster(sc, e=True, siv=joints)
    cmds.hilite(cmds.ls(sl=True, type='transform', r=True))


select_inf_vertex()