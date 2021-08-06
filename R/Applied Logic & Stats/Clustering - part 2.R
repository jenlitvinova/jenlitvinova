sids<- data.frame(read.csv("C:\\Users\\Yevgeniya Litvinova\\Documents\\SIW 004 Math and Stats\\final individual\\final_data.csv"))
#
group = sids[,1]
sids <- sids[,-1]
attach(sids)
#
par(mfrow=c(1,2))
plclust(hclust(dist(sids),method="single"),labels=row.names(sids),ylab="Distance")
title("(a) Single linkage")
plclust(hclust(dist(sids),method="complete"),labels=row.names(sids),ylab="Distance")
title("(b) Complete linkage")
#
two<-cutree(hclust(dist(sids),method="complete"),h=1600) #21 is the age threshold
#
sids.clus<-lapply(1:2,function(nc) row.names(sids)[two==nc])
sids.mean<-lapply(1:2,function(nc) apply(sids[two==nc,],2,mean))
#apply soemthing by 2 is apply an operation by columns (1 indicates rows)
#lapply - is the loop
#when the number of clusters is optimal there must be a difference in the means of the clusters
#within a cluster these values should be homogeneous
sids.mean
sids.clus
clus = c(1,2,2,2,1,1,2,2,1,1,1,2,1,1,1,2,2,1,1,1,1,2,1,2,1,1,1,2,2,1,2,1,2,2,1,1,2,2,2,2,1,1,2,1,1,2,2,1,2,2,1,2,1,1,1,2,1,1,2,1,1,1,1,1,1)
length(clus)

#
dev.off()
#
pairs(sids,panel=function(x,y) text(x,y,two)) 
#
table(group,clus)





#
five<-cutree(hclust(dist(sids),method="single"),h=200) #
sids.clus<-lapply(1:5,function(nc) row.names(sids)[five==nc])
sids.mean<-lapply(1:5,function(nc) apply(sids[five==nc,],2,mean))
sids.mean
sids.clus
clus = c(1,1,1,1,1,1,2,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,4,5,1,1,1,1,5,1,3,1,1,5,1,1)
length(clus)
#
dev.off()
#
pairs(sids,panel=function(x,y) text(x,y,two)) 
#
table(group,clus)
