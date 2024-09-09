package leetcode4;

public class LeetCode4 {

   public static double media(int a, int b) {
      return (a + b) / 2.0;
   }

   public static int partition(int[] arr, int l, int h) {
      int pivot = arr[h];
      int i = (l - 1);

      for (int j = l; j < h; j++) {
         if (arr[j] <= pivot) {
            i++;
            int vt = arr[i];
            arr[i] = arr[j];
            arr[j] = vt;
         }
      }
      int vt = arr[i + 1];
      arr[i + 1] = arr[h];
      arr[h] = vt;
      return i + 1;
   }

   public static void quickSort(int[] arr, int l, int h) {
      if (l < h) {
         int p = partition(arr, l, h);

         quickSort(arr, l, p - 1);
         quickSort(arr, p + 1, h);
      }
   }

   public static double findMedianSortedArrays(int[] nums1, int[] nums2) {
      int[] merged = new int[nums1.length + nums2.length];
      double mediana;

      for (int i = 0; i < nums1.length; i++) {
         merged[i] = nums1[i];
      }

      for (int j = 0; j < nums2.length; j++) {
         merged[j + nums1.length] = nums2[j];
      }
      quickSort(merged, 0, merged.length - 1);
      if (merged.length % 2 == 0) {
         mediana = media(
               merged[(merged.length / 2) - 1],
               merged[merged.length / 2]);
      } else {
         mediana = merged[Integer.valueOf(merged.length / 2)];
      }
      return mediana;
   }

   public static void main(String[] args) {
      int[] num1 = { 5, 3, 2 };
      int[] num2 = { 1, 6, 3 };
      System.out.println(findMedianSortedArrays(num1, num2));
   }
}
