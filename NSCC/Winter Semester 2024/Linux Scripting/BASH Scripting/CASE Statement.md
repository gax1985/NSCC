




case <variable> in  
  <pattern 1>)  
  <commands>  
  ;;  
  <pattern 2>)  
  <other commands>  
  ;;  
esac





>
>[!note]
>
>
>
>#!/bin/bash
># case example
> 
>case $1 in
>	start)
>		echo starting
>		;;
>	stop)
>		echo stopping
>		;;
>	restart)
>		echo restarting
>		;;
>	*)
>		echo don\'t know what I’m supposed to do
>		;;
>esac
>









