int rob(int* nums, int numsSize) {
    if (numsSize==0) return 0;
    if (3>= numsSize) return max(nums,numsSize));
	return max_two(robb(nums,0,numsSize-1),robb(nums,1,numsSize));
}

int linerob(nums,start,end){
	pre = nums[start];
	now = max(nums[start],nums[start+1]);
	for(i=start;i<end;i++) {
		now = max_two(nums[i]+pre,now);
		pre = now;
	}
	return now;
}

int max(nums,numsSize){
	max_val = nums[0];
	for(i=0;i<numsSize;i++){
		if (nums[i]>max_val) max_val=nums[i];
	}
	return max_val;
}

int max_two(val1,val2){
	if (val1 > val2)return val1;
	return val2;
}