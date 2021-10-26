\begin{itemize}
    \item Doing the first thing.
    \item Doing the second thing.
\end{itemize}

创建垂直居中的序号

	\begin{enumerate}[\bfseries 1.]
		\item We do ...
		\item We do ...
		\item We do ...
	\end{enumerate}
	
				\multicolumn{1}{m{2cm}}{\centering \textbf{Symbols}}\\
				
				&\multicolumn{1}{m{2cm}}{\centering \textbf{Unit}}\\
				
				&\multicolumn{1}{m{2cm}}{\centering \textbf{Description}}\\

$$斜体
$\alpha$
单独一行输入公式$$content$$（默认为斜体）
　　1，全局使用，使公式全部变为直体：
　　代码：\rm sigmod(x) = \frac{1} {1 + e^{-x}}
　　效果：sigmod(x)=11+e−x
　　2，局部使用，使公式一部分变为直体，该部分用{}括起来：
　　代码：{\rm sigmod}(x) = \frac{1} {1 + e^{-x}}
　　效果：sigmod(x)=11+e−x

上标$a^{i+j}$
下标$a_{i+j}$
点乘\cdot
输入方程
\begin{equation}\label{eq:heat}
sigmod(x) = \frac{1} {1 + e^{-x}}
\end{equation}

\begin{equation}\label{eq:heat}

\end{equation}

输入方程组
\begin{equation}\label{eq:heat}
	\begin{cases}
		l_{11}y_{1} = 1 \\
		l_{21}y_{1} + l_{22}y_{2} = 0 \\ 
		l_{31}y_{1} + l_{32}y_{2} + l_{33}y_{3} = 0 \\
		l_{41}y_{1} + l_ {42}y_{2} + l_{43}y_{3} + l_{44}y_{4} = 0
	\end{cases}
\end{equation}

插入图片
	\begin{figure}[htbp]
		\centering
		\includegraphics[width=.9\textwidth]{water.png}
		\caption{The result of Model 2}\label{fig:result}
	\end{figure}

创建多个图
	Figure \ref{fig:subfigures} gives an example of subfigures. Figure \ref{subfig:left} is on the left, and Figure \ref{subfig:right} is on the right.
	
	% ×ÓÍ¼£¨¶àÍ¼²¢ÁÐ£©Ê¾Àý£¬¸ü¶àÓÃ·¨Çë²Î¿¼ subfigure ºê°üÎÄµµ
	% Èç¹ûÄúÖ»Ï£Íû¼¸ÕÅÍ¼²¢ÁÐ£¬²»ÐèÒª¶îÍâµÄ caption£¬ÄÇÃ´ÔÚ figure »·¾³ÖÐ
	% Á¬Ðø²åÈë×Ü¿í¶È²»³¬¹ý \textwidth µÄ¶à¸ö \includegraphics ÃüÁî¼´¿É
	\begin{figure}[htbp]
		\centering
		\begin{subfigure}[b]{.4\textwidth}
			\includegraphics[width=\textwidth]{water.png}
			\caption{Image on the left}\label{subfig:left}
		\end{subfigure}
		\begin{subfigure}[b]{.4\textwidth}
			\includegraphics[width=\textwidth]{water.png}
			\caption{Image on the right}\label{subfig:right}
		\end{subfigure}
		\caption{Two images}\label{fig:subfigures}
	\end{figure}
\centering图片居中
figure参数：h 此处（here）t 页顶（top）b 页底（bottom）p 独立一页（page）

如何在section之间插入图片

任意连续空格被解释为一个空格
空行被解释为换行符
$转化为斜体字母
$$表示斜体字母并单独一行作为显示
$\$表示希腊字母
编辑数学公式的宏包：\usepackage{amsmath}和 \usepackage{amssymb}
编辑数学定理和证明过程的宏包：\usepackage{amsthm}
插入图片的宏包：\usepackage{graphicx}
复杂表格的宏包：\usepackage{multirow}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{amsthm}
\usepackage{graphicx}
\usepackage{multirow}