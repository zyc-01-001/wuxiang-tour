#!/usr/bin/env python3
"""
Add foyer (门厅) outside the entrance with openable double doors.
"""

with open('/workspace/wuxiang-tour/scene-memorial.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ========== 1. Replace the entrance door section with openable doors ==========
old_door = """    // ========== 入口大门 ==========
    const doorFrameMat = new THREE.MeshPhysicalMaterial({color:0x5c4033,roughness:0.5});
    const doorMat = new THREE.MeshPhysicalMaterial({color:0x3d2817,roughness:0.7});
    const doorGroup = new THREE.Group();
    const doorFrameL = new THREE.Mesh(new THREE.BoxGeometry(0.12,2.2,0.12), doorFrameMat);
    doorFrameL.position.set(-0.9,1.1,roomW/2);
    doorGroup.add(doorFrameL);
    const doorFrameR = new THREE.Mesh(new THREE.BoxGeometry(0.12,2.2,0.12), doorFrameMat);
    doorFrameR.position.set(0.9,1.1,roomW/2);
    doorGroup.add(doorFrameR);
    const doorFrameT = new THREE.Mesh(new THREE.BoxGeometry(2,0.12,0.12), doorFrameMat);
    doorFrameT.position.set(0,2.2,roomW/2);
    doorGroup.add(doorFrameT);
    const doorL = new THREE.Mesh(new THREE.BoxGeometry(0.85,2,0.06), doorMat);
    doorL.position.set(-0.45,1,roomW/2);
    doorGroup.add(doorL);
    const doorR = new THREE.Mesh(new THREE.BoxGeometry(0.85,2,0.06), doorMat);
    doorR.position.set(0.45,1,roomW/2);
    doorGroup.add(doorR);
    scene.add(doorGroup);"""

new_door = """    // ========== 门厅（展厅外小空间） ==========
    const foyerD = 3.5; // 门厅深度
    const foyerW = 3.0; // 门厅宽度
    const foyerH = 3.5; // 门厅高度

    // 门厅地面（深色石材）
    const foyerFloor = new THREE.Mesh(
        new THREE.BoxGeometry(foyerW, 0.05, foyerD),
        new THREE.MeshPhysicalMaterial({color: 0x3a3a3a, roughness: 0.6})
    );
    foyerFloor.position.set(0, 0.025, roomW/2 + foyerD/2);
    foyerFloor.receiveShadow = true;
    scene.add(foyerFloor);

    // 门厅天花板
    const foyerCeiling = new THREE.Mesh(
        new THREE.BoxGeometry(foyerW, 0.05, foyerD),
        new THREE.MeshPhysicalMaterial({color: 0xf5f5f0, roughness: 0.9})
    );
    foyerCeiling.position.set(0, foyerH, roomW/2 + foyerD/2);
    scene.add(foyerCeiling);

    // 门厅两侧短墙
    const foyerWallMat = new THREE.MeshPhysicalMaterial({color: 0x8b7355, roughness: 0.85});
    const foyerWallL = new THREE.Mesh(new THREE.BoxGeometry(0.15, foyerH, foyerD), foyerWallMat);
    foyerWallL.position.set(-foyerW/2 + 0.075, foyerH/2, roomW/2 + foyerD/2);
    scene.add(foyerWallL);
    const foyerWallR = new THREE.Mesh(new THREE.BoxGeometry(0.15, foyerH, foyerD), foyerWallMat);
    foyerWallR.position.set(foyerW/2 - 0.075, foyerH/2, roomW/2 + foyerD/2);
    scene.add(foyerWallR);

    // 门厅前墙（只有门框，中间是大门）
    const frontWallL = new THREE.Mesh(new THREE.BoxGeometry(0.6, foyerH, 0.15), foyerWallMat);
    frontWallL.position.set(-foyerW/2 + 0.3, foyerH/2, roomW/2 + foyerD);
    scene.add(frontWallL);
    const frontWallR = new THREE.Mesh(new THREE.BoxGeometry(0.6, foyerH, 0.15), foyerWallMat);
    frontWallR.position.set(foyerW/2 - 0.3, foyerH/2, roomW/2 + foyerD);
    scene.add(frontWallR);
    const frontWallT = new THREE.Mesh(new THREE.BoxGeometry(foyerW - 1.2, 0.8, 0.15), foyerWallMat);
    frontWallT.position.set(0, foyerH - 0.4, roomW/2 + foyerD);
    scene.add(frontWallT);

    // 门厅迎宾灯
    const foyerLight = new THREE.PointLight(0xfff5e6, 0.6, 6);
    foyerLight.position.set(0, 2.8, roomW/2 + foyerD/2);
    scene.add(foyerLight);

    // ========== 可开合双开门 ==========
    const doorFrameMat = new THREE.MeshPhysicalMaterial({color:0x5c4033,roughness:0.5});
    const doorMat = new THREE.MeshPhysicalMaterial({color:0x3d2817,roughness:0.7});

    // 门框（固定在展厅墙上）
    const doorFrameL = new THREE.Mesh(new THREE.BoxGeometry(0.12,2.2,0.12), doorFrameMat);
    doorFrameL.position.set(-0.9,1.1,roomW/2);
    scene.add(doorFrameL);
    const doorFrameR = new THREE.Mesh(new THREE.BoxGeometry(0.12,2.2,0.12), doorFrameMat);
    doorFrameR.position.set(0.9,1.1,roomW/2);
    scene.add(doorFrameR);
    const doorFrameT = new THREE.Mesh(new THREE.BoxGeometry(2,0.12,0.12), doorFrameMat);
    doorFrameT.position.set(0,2.2,roomW/2);
    scene.add(doorFrameT);

    // 左门扇（可旋转）- 旋转轴在左侧
    doorLeftGroup = new THREE.Group();
    doorLeftGroup.position.set(-0.85, 0, roomW/2); // 旋转轴位置
    const doorL = new THREE.Mesh(new THREE.BoxGeometry(0.85,2,0.06), doorMat);
    doorL.position.set(0.425, 1, 0); // 门扇中心相对于旋转轴
    doorL.castShadow = true;
    doorLeftGroup.add(doorL);
    scene.add(doorLeftGroup);

    // 右门扇（可旋转）- 旋转轴在右侧
    doorRightGroup = new THREE.Group();
    doorRightGroup.position.set(0.85, 0, roomW/2); // 旋转轴位置
    const doorR = new THREE.Mesh(new THREE.BoxGeometry(0.85,2,0.06), doorMat);
    doorR.position.set(-0.425, 1, 0); // 门扇中心相对于旋转轴
    doorR.castShadow = true;
    doorRightGroup.add(doorR);
    scene.add(doorRightGroup);

    // 门把手
    const handleMat = new THREE.MeshPhysicalMaterial({color:0xd4a853,metalness:0.9,roughness:0.2});
    const handleL = new THREE.Mesh(new THREE.SphereGeometry(0.04,8,8), handleMat);
    handleL.position.set(0.75, 1, 0.04);
    doorLeftGroup.add(handleL);
    const handleR = new THREE.Mesh(new THREE.SphereGeometry(0.04,8,8), handleMat);
    handleR.position.set(-0.75, 1, 0.04);
    doorRightGroup.add(handleR);

    // 将门添加为可交互对象
    doorLeftGroup.userData = { itemName: '展厅大门', isDoor: true, side: 'left' };
    doorRightGroup.userData = { itemName: '展厅大门', isDoor: true, side: 'right' };
    interactiveObjects.push(doorLeftGroup);
    interactiveObjects.push(doorRightGroup);"""

content = content.replace(old_door, new_door)
print("Added foyer and openable doors")

# ========== 2. Add global door variables and animation ==========
# Find a good place to add door globals - after the other globals
old_globals = """let selectedObject = null;
let currentItem = null;"""

new_globals = """let selectedObject = null;
let currentItem = null;
let doorLeftGroup = null;
let doorRightGroup = null;
let doorOpen = false;
let doorAnimating = false;"""

content = content.replace(old_globals, new_globals)
print("Added door global variables")

# ========== 3. Add door animation and interaction functions ==========
door_functions = """
// ========== 门动画 ==========
function animateDoorOpen() {
    if(doorAnimating || doorOpen) return;
    doorAnimating = true;
    const duration = 1500;
    const start = performance.now();
    function animate(now) {
        const t = Math.min((now - start) / duration, 1);
        const ease = 1 - Math.pow(1 - t, 3); // ease-out
        // 左门向外旋转90度（负y方向）
        doorLeftGroup.rotation.y = -ease * Math.PI / 2;
        // 右门向外旋转90度（正y方向）
        doorRightGroup.rotation.y = ease * Math.PI / 2;
        if(t < 1) {
            requestAnimationFrame(animate);
        } else {
            doorOpen = true;
            doorAnimating = false;
        }
    }
    requestAnimationFrame(animate);
}

function animateDoorClose() {
    if(doorAnimating || !doorOpen) return;
    doorAnimating = true;
    const duration = 1200;
    const start = performance.now();
    function animate(now) {
        const t = Math.min((now - start) / duration, 1);
        const ease = 1 - Math.pow(1 - t, 3);
        doorLeftGroup.rotation.y = -Math.PI / 2 * (1 - ease);
        doorRightGroup.rotation.y = Math.PI / 2 * (1 - ease);
        if(t < 1) {
            requestAnimationFrame(animate);
        } else {
            doorOpen = false;
            doorAnimating = false;
        }
    }
    requestAnimationFrame(animate);
}

"""

# Insert before createMaterials function
content = content.replace("function createMaterials() {", door_functions + "function createMaterials() {")
print("Added door animation functions")

# ========== 4. Update onKeyDown to handle door interaction ==========
old_key_e = """        case 'KeyE':
            if (isLocked && hoveredObject) {
                openItemPanel(hoveredObject);
            }
            break;"""

new_key_e = """        case 'KeyE':
            if (isLocked && hoveredObject) {
                if(hoveredObject.userData.isDoor) {
                    if(doorOpen) {
                        animateDoorClose();
                    } else {
                        animateDoorOpen();
                    }
                } else {
                    openItemPanel(hoveredObject);
                }
            }
            break;"""

content = content.replace(old_key_e, new_key_e)
print("Updated E key for door interaction")

# ========== 5. Update checkItemFocus to show door hint ==========
old_hint = """        if(isMobile){
            mobileBtn.classList.add('visible');
            interactHint.classList.remove('visible');
        }else{
            interactHint.classList.add('visible');
            mobileBtn.classList.remove('visible');
        }"""

new_hint = """        if(isMobile){
            mobileBtn.classList.add('visible');
            interactHint.classList.remove('visible');
        }else{
            interactHint.classList.add('visible');
            // 门显示特殊提示
            if(obj.userData.isDoor) {
                interactHint.textContent = doorOpen ? '按 E 关闭大门' : '按 E 打开大门';
            } else {
                interactHint.textContent = '按 E 查看展品';
            }
            mobileBtn.classList.remove('visible');
        }"""

content = content.replace(old_hint, new_hint)
print("Updated door interaction hint")

# ========== 6. Update player start position to outside the door ==========
old_start = """    // 相机初始位置（入口附近）
    camera.position.set(0, PLAYER_HEIGHT, roomD/2 - 1.5);"""

new_start = """    // 相机初始位置（门厅外）
    camera.position.set(0, PLAYER_HEIGHT, roomD/2 + 2.5);"""

content = content.replace(old_start, new_start)
print("Moved player start to foyer")

# ========== 7. Update control hint to show door info ==========
content = content.replace(
    '<div class="control-row"><span class="key">WASD</span> 移动 &nbsp;|&nbsp; <span class="key">鼠标</span> 环视</div>',
    '<div class="control-row"><span class="key">WASD</span> 移动 &nbsp;|&nbsp; <span class="key">鼠标</span> 环视 &nbsp;|&nbsp; <span class="key">E</span> 开门/查看展品</div>'
)
print("Updated control hints")

with open('/workspace/wuxiang-tour/scene-memorial.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nFoyer and door system complete!")
