def two_sum(nums, target):
    # قاموس لتخزين الأرقام التي تم مشاهدتها سابقًا وفهارسها
    seen = {}
    
    # استخدام حلقة while للتكرار عبر الأرقام
    i = 0
    while i < len(nums):
        # حساب الفرق المطلوب للوصول إلى الهدف
        diff = target - nums[i]
        
        # التحقق مما إذا كان الفرق موجودًا بالفعل في القاموس
        if diff in seen:
            return [seen[diff], i]
        
        # إذا لم يكن موجودًا، تخزين الرقم الحالي وفهرسه في القاموس
        seen[nums[i]] = i
        
        # زيادة الفهرس يدويًا
        i += 1

# مثال 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))  # الناتج: [0, 1]

# مثال 2
nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))  # الناتج: [1, 2]

# مثال 3
nums3 = [3, 3]
target3 = 6
print(two_sum(nums3, target3))  # الناتج: [0, 1]

######################################################


##########################################################
def two_sum(nums, target):
    # حلقة أولى تمر على كل عنصر في المصفوفة
    for i in range(len(nums)):
        # حلقة ثانية تبدأ من العنصر التالي للعنصر الحالي
        for j in range(i + 1, len(nums)):
            # التحقق إذا كان مجموع العنصرين يساوي الهدف
            if nums[i] + nums[j] == target:
                return [i, j]
# مثال 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(two_sum(nums1, target1))  # Output: [0, 1]

# Exempel 2:
nums2 = [3, 2, 4]
target2 = 6
print(two_sum(nums2, target2))  # Output: [1, 2]

# Exempel 3:
nums3 = [3, 3]
target3 = 6
print(two_sum(nums3, target3))  # Output: [0, 1]