object PracticeOneApp
{
    def bubbleSort(arr: Array[Int]) : Array[Int] = 
    {
        for(i <- 0 until arr.length)
        {
            for(j <- 0 until arr.length - i - 1)
            {
                if(arr(j) > arr(j+1))
                {
                    val temp = arr(j)
                    arr(j) = arr(j + 1)
                    arr(j+1) = temp
                }
            }
        }
        arr
    }

    def main(args : Array[String]) : Unit = 
    {
        val arr = Array(5 ,  2  , 5 , 8 , 9)
        println("\nOrignalArray : ")
        println(arr.mkString(","))

        val newArr = bubbleSort(arr)
        println("\nSortedArray : ")
        println(newArr.mkString(","))
    }
}