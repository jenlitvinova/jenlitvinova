sids<- data.frame(read.csv("C:\\Users\\Yevgeniya Litvinova\\Documents\\SIW 004 Math and Stats\\final individual\\final_data.csv"))
#
sids <- sids[,-1]
attach(sids)
sids#
pairs(sids[,-1])

#
#
cor(sids[,-1]) 
sids.pc<-princomp(sids[,-1],cor=TRUE)
#
summary(sids.pc,loadings=TRUE)
#
sids.pc$scores[,1:2]
#
par(mfrow=c(1,2))
plot(sids.pc$scores[,1],HR,xlab="PC1")
plot(sids.pc$scores[,2],HR,xlab="PC2")
#
dev.off()
#
par(pty="s")
plot(sids.pc$score[,1],sids.pc$scores[,2],
ylim=range(sids.pc$score[,1]),
xlab="PC1",ylab="PC2",type="n",lwd=2)
text(sids.pc$score[,1],sids.pc$score[,2],
labels=abbreviate(row.names(sids)),cex=0.7,lwd=2)
#
#
summary(lm(HR~sids.pc$score[,1]+sids.pc$score[,2]))
#
#
load(lqs)
#
usair.mve<-cov.mve(usair.dat[,-1],cor=TRUE)
#
usair.mve$cor
usair.pc1<-princomp(usair.dat[,-1],covlist=usair.mve,cor=TRUE)
summary(usair.pc1,loadings=T)
#
#
#Chapter 8
usair.fit<-lm(SO2~Neg.Temp+Manuf+Pop+Wind+Precip+Days)
summary(usair.fit)
