import os
class FFMpegUtil(object):
	def __init__(self):
		pass

	def createFFMpehPath(self,dicname):
		filedic='../result/ComparaPic/'+dicname
		if os.path.exists(filedic)==False:
			os.makedirs(filedic)


	def getConparaPicPath(self):
		path=os.path.dirname(os.path.realpath(__file__))
		return path[:path.rindex('\\')]+"\ComparaPic"

	def getResultFilePath(self,dirname):
		path=os.path.dirname(os.path.realpath(__file__))
		return path[:path.rindex('\\')]+"\\Result\\"+dirname


	def getVideoPath(self,videoname):

		pass

	def runFFMpeg(self):
		videopath=self.getResultFilePath('video')
		comparapath=self.getResultFilePath('ComparaPic')
		cmd=''



if __name__=='__main__':
	f=FFMpegUtil()
	# f.createFFMpehPath('dddd')
	print(f.getResultFilePath('Video'))
