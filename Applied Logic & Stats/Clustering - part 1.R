sids<- data.frame(read.csv("C:\\Users\\Yevgeniya Litvinova\\Documents\\SIW 004 Math and Stats\\final individual\\final_data.csv"))
#
group = sids[,1]
sids <- sids[,-1]
attach(sids)
#

matrix.sids <- matrix(c(sids[,1],sids[,2],sids[,3],sids[,4]), ncol = 4)

#typification
sd.vector = apply (sids,2,sd)
mean.vector = apply(sids, 2, mean)

top = (apply(sids,2, function(x) x) -apply(sids, 2, mean))
sd = apply (sids,2,sd)
sids.dat<-sweep(top,2,sd,FUN="/") #the ratio of the original data by range ( to normalize the data)
#sweep is from the original data by columns we perform a particulate function 
#the best normalization procedure is
#given the data x
#             _
#     z = x - x
#1)   ---------       = typification - the most complete type of normalization
#     s (or sqrt(var))
#
#2)      x
#   z = ---	
#	 s^2
#
#3)      x
#   z = ----
#	range
#
####Range
rge<-apply(sids,2,max)-apply(sids,2,min)
sids.dat<-sweep(sids,2,rge,FUN="/")


n<-length(sids.dat[,1])	
wss1<-(n-1)*sum(apply(sids.dat,2,var))
wss<-numeric(0)
for(i in 2:6) {
	   W<-sum(kmeans(sids.dat,i)$withinss)
	   wss<-c(wss,W)
}
#
wss<-c(wss1,wss)
plot(1:6,wss,type="l",xlab="Number of groups",ylab="Within groups sum of squares",lwd=2)
# 	
sids.kmean<-kmeans(sids.dat,2)
sids.kmean
kmeans(sids.dat, 2)$cluster #shows which observation belongs to which cluster)
lapply(1:2,function(nc) apply(sids[sids.kmean$cluster==nc,],2,mean))
#
#
table(group,sids.kmean$cluster)
comp = cbind (sids,group, "kmean cluster" = sids.kmean$cluster)
#
u  
