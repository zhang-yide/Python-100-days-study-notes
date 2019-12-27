# [术语对照表](https://docs.python.org/zh-cn/3/glossary.html)

- `>>>`

  交互式终端中默认的 Python 提示符。往往会显示于能以交互方式在解释器里执行的样例代码之前。

- `...`

  可以是指：交互式终端中输入特殊代码行时默认的 Python 提示符，包括：缩进的代码块，成对的分隔符之内（圆括号、方括号、花括号或三重引号），或是指定一个装饰器之后。[`Ellipsis`](https://docs.python.org/zh-cn/3/library/constants.html#Ellipsis) 内置常量。

- 2to3

  一个将 Python 2.x 代码转换为 Python 3.x 代码的工具，能够处理大部分通过解析源码并遍历解析树可检测到的不兼容问题。2to3 包含在标准库中，模块名为 [`lib2to3`](https://docs.python.org/zh-cn/3/library/2to3.html#module-lib2to3)；并提供一个独立入口点 `Tools/scripts/2to3`。参见 [2to3 - 自动将 Python 2 代码转为 Python 3 代码](https://docs.python.org/zh-cn/3/library/2to3.html#to3-reference)。

- abstract base class -- 抽象基类

  抽象基类简称 ABC，是对 [duck-typing](https://docs.python.org/zh-cn/3/glossary.html#term-duck-typing) 的补充，它提供了一种定义接口的新方式，相比之下其他技巧例如 [`hasattr()`](https://docs.python.org/zh-cn/3/library/functions.html#hasattr) 显得过于笨拙或有微妙错误（例如使用 [魔术方法](https://docs.python.org/zh-cn/3/reference/datamodel.html#special-lookup)）。ABC 引入了虚拟子类，这种类并非继承自其他类，但却仍能被 [`isinstance()`](https://docs.python.org/zh-cn/3/library/functions.html#isinstance) 和 [`issubclass()`](https://docs.python.org/zh-cn/3/library/functions.html#issubclass) 所认可；详见 [`abc`](https://docs.python.org/zh-cn/3/library/abc.html#module-abc) 模块文档。Python 自带许多内置的 ABC 用于实现数据结构（在 [`collections.abc`](https://docs.python.org/zh-cn/3/library/collections.abc.html#module-collections.abc) 模块中）、数字（在 [`numbers`](https://docs.python.org/zh-cn/3/library/numbers.html#module-numbers) 模块中）、流（在 [`io`](https://docs.python.org/zh-cn/3/library/io.html#module-io) 模块中）、导入查找器和加载器（在 [`importlib.abc`](https://docs.python.org/zh-cn/3/library/importlib.html#module-importlib.abc) 模块中）。你可以使用 [`abc`](https://docs.python.org/zh-cn/3/library/abc.html#module-abc) 模块来创建自己的 ABC。

- annotation -- 注解

  关联到某个变量、类属性、函数形参或返回值的标签，被约定作为 [type hint](https://docs.python.org/zh-cn/3/glossary.html#term-type-hint) 来使用。局部变量的标注在运行时不可访问，但全局变量、类属性和函数的标注会分别存放模块、类和函数的 `__annotations__` 特殊属性中。参见 [variable annotation](https://docs.python.org/zh-cn/3/glossary.html#term-variable-annotation)、[function annotation](https://docs.python.org/zh-cn/3/glossary.html#term-function-annotation)、[**PEP 484**](https://www.python.org/dev/peps/pep-0484) 和 [**PEP 526**](https://www.python.org/dev/peps/pep-0526)，对此功能均有介绍。

- argument -- 参数

  在调用函数时传给 [function](https://docs.python.org/zh-cn/3/glossary.html#term-function) （或 [method](https://docs.python.org/zh-cn/3/glossary.html#term-method) ）的值。参数分为两种：*关键字参数*: 在函数调用中前面带有标识符（例如 `name=`）或者作为包含在前面带有 `**` 的字典里的值传入。举例来说，`3` 和 `5` 在以下对 [`complex()`](https://docs.python.org/zh-cn/3/library/functions.html#complex) 的调用中均属于关键字参数:`complex(real=3, imag=5) complex(**{'real': 3, 'imag': 5}) `*位置参数*: 不属于关键字参数的参数。位置参数可出现于参数列表的开头以及/或者作为前面带有 `*` 的 [iterable](https://docs.python.org/zh-cn/3/glossary.html#term-iterable) 里的元素被传入。举例来说，`3` 和 `5` 在以下调用中均属于位置参数:`complex(3, 5) complex(*(3, 5)) `参数会被赋值给函数体中对应的局部变量。有关赋值规则参见 [调用](https://docs.python.org/zh-cn/3/reference/expressions.html#calls) 一节。根据语法，任何表达式都可用来表示一个参数；最终算出的值会被赋给对应的局部变量。另参见 [parameter](https://docs.python.org/zh-cn/3/glossary.html#term-parameter) 术语表条目，常见问题中 [参数与形参的区别](https://docs.python.org/zh-cn/3/faq/programming.html#faq-argument-vs-parameter) 以及 [**PEP 362**](https://www.python.org/dev/peps/pep-0362)。

- asynchronous context manager -- 异步上下文管理器

  此种对象通过定义 [`__aenter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__aenter__) 和 [`__aexit__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__aexit__) 方法来对 [`async with`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-with) 语句中的环境进行控制。由 [**PEP 492**](https://www.python.org/dev/peps/pep-0492) 引入。

- asynchronous generator -- 异步生成器

  返回值为 [asynchronous generator iterator](https://docs.python.org/zh-cn/3/glossary.html#term-asynchronous-generator-iterator) 的函数。它与使用 [`async def`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-def) 定义的协程函数很相似，不同之处在于它包含 [`yield`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#yield) 表达式以产生一系列可在 [`async for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-for) 循环中使用的值。此术语通常是指异步生成器函数，但在某些情况下则可能是指 *异步生成器迭代器*。如果需要清楚表达具体含义，请使用全称以避免歧义。一个异步生成器函数可能包含 [`await`](https://docs.python.org/zh-cn/3/reference/expressions.html#await) 表达式或者 [`async for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-for) 以及 [`async with`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-with) 语句。

- asynchronous generator iterator -- 异步生成器迭代器

  [asynchronous generator](https://docs.python.org/zh-cn/3/glossary.html#term-asynchronous-generator) 函数所创建的对象。此对象属于 [asynchronous iterator](https://docs.python.org/zh-cn/3/glossary.html#term-asynchronous-iterator)，当使用 [`__anext__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__anext__) 方法调用时会返回一个可等待对象来执行异步生成器函数的代码直到下一个 [`yield`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#yield) 表达式。每个 [`yield`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#yield) 会临时暂停处理，记住当前位置执行状态 (包括局部变量和挂起的 try 语句)。当该 *异步生成器迭代器* 与其他 [`__anext__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__anext__) 返回的可等待对象有效恢复时，它会从离开位置继续执行。参见 [**PEP 492**](https://www.python.org/dev/peps/pep-0492) 和 [**PEP 525**](https://www.python.org/dev/peps/pep-0525)。

- asynchronous iterable -- 异步可迭代对象

  可在 [`async for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-for) 语句中被使用的对象。必须通过它的 [`__aiter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__aiter__) 方法返回一个 [asynchronous iterator](https://docs.python.org/zh-cn/3/glossary.html#term-asynchronous-iterator)。由 [**PEP 492**](https://www.python.org/dev/peps/pep-0492) 引入。

- asynchronous iterator -- 异步迭代器

  实现了 [`__aiter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__aiter__) 和 [`__anext__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__anext__) 方法的对象。`__anext__` 必须返回一个 [awaitable](https://docs.python.org/zh-cn/3/glossary.html#term-awaitable) 对象。[`async for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-for) 会处理异步迭代器的 [`__anext__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__anext__) 方法所返回的可等待对象，直到其引发一个 [`StopAsyncIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopAsyncIteration) 异常。由 [**PEP 492**](https://www.python.org/dev/peps/pep-0492) 引入。

- attribute -- 属性

  关联到一个对象的值，可以使用点号表达式通过其名称来引用。例如，如果一个对象 *o* 具有一个属性 *a*，就可以用 *o.a* 来引用它。

- awaitable -- 可等待对象

  能在 [`await`](https://docs.python.org/zh-cn/3/reference/expressions.html#await) 表达式中使用的对象。可以是 [coroutine](https://docs.python.org/zh-cn/3/glossary.html#term-coroutine) 或是具有 [`__await__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__await__) 方法的对象。参见 [**PEP 492**](https://www.python.org/dev/peps/pep-0492)。

- BDFL

  “终身仁慈独裁者”的英文缩写，即 [Guido van Rossum](https://gvanrossum.github.io/)，Python 的创造者。

- binary file -- 二进制文件

  [file object](https://docs.python.org/zh-cn/3/glossary.html#term-file-object) 能够读写 [字节类对象](https://docs.python.org/zh-cn/3/glossary.html#term-bytes-like-object)。二进制文件的例子包括以二进制模式（`'rb'`, `'wb'` or `'rb+'`）打开的文件、`sys.stdin.buffer`、`sys.stdout.buffer` 以及 [`io.BytesIO`](https://docs.python.org/zh-cn/3/library/io.html#io.BytesIO) 和 [`gzip.GzipFile`](https://docs.python.org/zh-cn/3/library/gzip.html#gzip.GzipFile) 的实例。另请参见 [text file](https://docs.python.org/zh-cn/3/glossary.html#term-text-file) 了解能够读写 [`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 对象的文件对象。

- bytes-like object -- 字节类对象

  支持 [缓冲协议](https://docs.python.org/zh-cn/3/c-api/buffer.html#bufferobjects) 并且能导出 C-[contiguous](https://docs.python.org/zh-cn/3/glossary.html#term-contiguous) 缓冲的对象。这包括所有 [`bytes`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes)、[`bytearray`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytearray) 和 [`array.array`](https://docs.python.org/zh-cn/3/library/array.html#array.array) 对象，以及许多普通 [`memoryview`](https://docs.python.org/zh-cn/3/library/stdtypes.html#memoryview) 对象。字节类对象可在多种二进制数据操作中使用；这些操作包括压缩、保存为二进制文件以及通过套接字发送等。某些操作需要可变的二进制数据。这种对象在文档中常被称为“可读写字节类对象”。可变缓冲对象的例子包括 [`bytearray`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytearray) 以及 [`bytearray`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytearray) 的 [`memoryview`](https://docs.python.org/zh-cn/3/library/stdtypes.html#memoryview)。其他操作要求二进制数据存放于不可变对象 ("只读字节类对象")；这种对象的例子包括 [`bytes`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes) 以及 [`bytes`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes) 对象的 [`memoryview`](https://docs.python.org/zh-cn/3/library/stdtypes.html#memoryview)。

- bytecode -- 字节码

  Python 源代码会被编译为字节码，即 CPython 解释器中表示 Python 程序的内部代码。字节码还会缓存在 `.pyc` 文件中，这样第二次执行同一文件时速度更快（可以免去将源码重新编译为字节码）。这种 "中间语言" 运行在根据字节码执行相应机器码的 [virtual machine](https://docs.python.org/zh-cn/3/glossary.html#term-virtual-machine) 之上。请注意不同 Python 虚拟机上的字节码不一定通用，也不一定能在不同 Python 版本上兼容。字节码指令列表可以在 [dis 模块](https://docs.python.org/zh-cn/3/library/dis.html#bytecodes) 的文档中查看。

- class -- 类

  用来创建用户定义对象的模板。类定义通常包含对该类的实例进行操作的方法定义。

- class variable -- 类变量

  在类中定义的变量，并且仅限在类的层级上修改 (而不是在类的实例中修改)。

- coercion -- 强制类型转换

  在包含两个相同类型参数的操作中，一种类型的实例隐式地转换为另一种类型。例如，`int(3.15)` 是将原浮点数转换为整型数 `3`，但在 `3+4.5` 中，参数的类型不一致（一个是 int, 一个是 float），两者必须转换为相同类型才能相加，否则将引发 [`TypeError`](https://docs.python.org/zh-cn/3/library/exceptions.html#TypeError)。如果没有强制类型转换机制，程序员必须将所有可兼容参数归一化为相同类型，例如要写成 `float(3)+4.5` 而不是 `3+4.5`。

- complex number -- 复数

  对普通实数系统的扩展，其中所有数字都被表示为一个实部和一个虚部的和。虚数是虚数单位（`-1` 的平方根）的实倍数，通常在数学中写为 `i`，在工程学中写为 `j`。Python 内置了对复数的支持，采用工程学标记方式；虚部带有一个 `j` 后缀，例如 `3+1j`。如果需要 [`math`](https://docs.python.org/zh-cn/3/library/math.html#module-math) 模块内对象的对应复数版本，请使用 [`cmath`](https://docs.python.org/zh-cn/3/library/cmath.html#module-cmath)，复数的使用是一个比较高级的数学特性。如果你感觉没有必要，忽略它们也几乎不会有任何问题。

- context manager -- 上下文管理器

  在 [`with`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#with) 语句中使用，通过定义 [`__enter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__enter__) 和 [`__exit__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__exit__) 方法来控制环境状态的对象。参见 [**PEP 343**](https://www.python.org/dev/peps/pep-0343)。

- context variable -- 上下文变量

  一种根据其所属的上下文可以具有不同的值的变量。 这类似于在线程局部存储中每个执行线程可以具有不同的变量值。 不过，对于上下文变量来说，一个执行线程中可能会有多个上下文，而上下文变量的主要用途是对并发异步任务中变量进行追踪。 参见 [`contextvars`](https://docs.python.org/zh-cn/3/library/contextvars.html#module-contextvars)。

- contiguous -- 连续

  一个缓冲如果是 *C 连续* 或 *Fortran 连续* 就会被认为是连续的。零维缓冲是 C 和 Fortran 连续的。在一维数组中，所有条目必须在内存中彼此相邻地排列，采用从零开始的递增索引顺序。在多维 C-连续数组中，当按内存地址排列时用最后一个索引访问条目时速度最快。但是在 Fortran 连续数组中则是用第一个索引最快。

- coroutine -- 协程

  协程是子例程的更一般形式。 子例程可以在某一点进入并在另一点退出。 协程则可以在许多不同的点上进入、退出和恢复。 它们可通过 [`async def`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-def) 语句来实现。 参见 [**PEP 492**](https://www.python.org/dev/peps/pep-0492)。

- coroutine function -- 协程函数

  返回一个 [coroutine](https://docs.python.org/zh-cn/3/glossary.html#term-coroutine) 对象的函数。协程函数可通过 [`async def`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-def) 语句来定义，并可能包含 [`await`](https://docs.python.org/zh-cn/3/reference/expressions.html#await)、[`async for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-for) 和 [`async with`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#async-with) 关键字。这些特性是由 [**PEP 492**](https://www.python.org/dev/peps/pep-0492) 引入的。

- CPython

  Python 编程语言的规范实现，在 [python.org](https://www.python.org/) 上发布。"CPython" 一词用于在必要时将此实现与其他实现例如 Jython 或 IronPython 相区别。

- decorator -- 装饰器

  返回值为另一个函数的函数，通常使用 `@wrapper` 语法形式来进行函数变换。 装饰器的常见例子包括 [`classmethod()`](https://docs.python.org/zh-cn/3/library/functions.html#classmethod) 和 [`staticmethod()`](https://docs.python.org/zh-cn/3/library/functions.html#staticmethod)。装饰器语法只是一种语法糖，以下两个函数定义在语义上完全等价:`def f(...):    ... f = staticmethod(f) @staticmethod def f(...):    ... `同的样概念也适用于类，但通常较少这样使用。有关装饰器的详情可参见 [函数定义](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#function) 和 [类定义](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#class) 的文档。

- descriptor -- 描述器

  任何定义了 [`__get__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__get__), [`__set__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__set__) 或 [`__delete__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__delete__) 方法的对象。当一个类属性为描述器时，它的特殊绑定行为就会在属性查找时被触发。通常情况下，使用 *a.b* 来获取、设置或删除一个属性时会在 *a* 的类字典中查找名称为 *b* 的对象，但如果 *b* 是一个描述器，则会调用对应的描述器方法。理解描述器的概念是更深层次理解 Python 的关键，因为这是许多重要特性的基础，包括函数、方法、属性、类方法、静态方法以及对超类的引用等等。有关描述符的方法的详情可参看 [实现描述器](https://docs.python.org/zh-cn/3/reference/datamodel.html#descriptors)。

- dictionary -- 字典

  一个关联数组，其中的任意键都映射到相应的值。键可以是任何具有 [`__hash__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__hash__) 和 [`__eq__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__eq__) 方法的对象。在 Perl 语言中称为 hash。

- dictionary view -- 字典视图

  从 [`dict.keys()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict.keys), [`dict.values()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict.values) 和 [`dict.items()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict.items) 返回的对象被称为字典视图。它们提供了字典条目的一个动态视图，这意味着当字典改变时，视图也会相应改变。要将字典视图强制转换为真正的列表，可使用 `list(dictview)`。参见 [字典视图对象](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict-views)。

- docstring -- 文档字符串

  作为类、函数或模块之内的第一个表达式出现的字符串字面值。它在代码执行时会被忽略，但会被解释器识别并放入所在类、函数或模块的 `__doc__` 属性中。由于它可用于代码内省，因此是对象存放文档的规范位置。

- duck-typing -- 鸭子类型

  指一种编程风格，它并不依靠查找对象类型来确定其是否具有正确的接口，而是直接调用或使用其方法或属性（“看起来像鸭子，叫起来也像鸭子，那么肯定就是鸭子。”）由于强调接口而非特定类型，设计良好的代码可通过允许多态替代来提升灵活性。鸭子类型避免使用 [`type()`](https://docs.python.org/zh-cn/3/library/functions.html#type) 或 [`isinstance()`](https://docs.python.org/zh-cn/3/library/functions.html#isinstance) 检测。(但要注意鸭子类型可以使用 [抽象基类](https://docs.python.org/zh-cn/3/glossary.html#term-abstract-base-class) 作为补充。) 而往往会采用 [`hasattr()`](https://docs.python.org/zh-cn/3/library/functions.html#hasattr) 检测或是 [EAFP](https://docs.python.org/zh-cn/3/glossary.html#term-eafp) 编程。

- EAFP

  “求原谅比求许可更容易”的英文缩写。这种 Python 常用代码编写风格会假定所需的键或属性存在，并在假定错误时捕获异常。这种简洁快速风格的特点就是大量运用 [`try`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#try) 和 [`except`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#except) 语句。于其相对的则是所谓 [LBYL](https://docs.python.org/zh-cn/3/glossary.html#term-lbyl) 风格，常见于 C 等许多其他语言。

- expression -- 表达式

  可以求出某个值的语法单元。 换句话说，一个表达式就是表达元素例如字面值、名称、属性访问、运算符或函数调用的汇总，它们最终都会返回一个值。 与许多其他语言不同，并非所有语言构件都是表达式。 还存在不能被用作表达式的 [statement](https://docs.python.org/zh-cn/3/glossary.html#term-statement)，例如 [`while`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#while)。 赋值也是属于语句而非表达式。

- extension module -- 扩展模块

  以 C 或 C++ 编写的模块，使用 Python 的 C API 来与语言核心以及用户代码进行交互。

- f-string -- f-字符串

  带有 `'f'` 或 `'F'` 前缀的字符串字面值通常被称为“f-字符串”即 [格式化字符串字面值](https://docs.python.org/zh-cn/3/reference/lexical_analysis.html#f-strings) 的简写。参见 [**PEP 498**](https://www.python.org/dev/peps/pep-0498)。

- file object -- 文件对象

  对外提供面向文件 API 以使用下层资源的对象（带有 `read()` 或 `write()` 这样的方法）。根据其创建方式的不同，文件对象可以处理对真实磁盘文件，对其他类型存储，或是对通讯设备的访问（例如标准输入/输出、内存缓冲区、套接字、管道等等）。文件对象也被称为 *文件类对象* 或 *流*。实际上共有三种类别的文件对象: 原始 [二进制文件](https://docs.python.org/zh-cn/3/glossary.html#term-binary-file), 缓冲 [二进制文件](https://docs.python.org/zh-cn/3/glossary.html#term-binary-file) 以及 [文本文件](https://docs.python.org/zh-cn/3/glossary.html#term-text-file)。它们的接口定义均在 [`io`](https://docs.python.org/zh-cn/3/library/io.html#module-io) 模块中。创建文件对象的规范方式是使用 [`open()`](https://docs.python.org/zh-cn/3/library/functions.html#open) 函数。

- file-like object -- 文件类对象

  [file object](https://docs.python.org/zh-cn/3/glossary.html#term-file-object) 的同义词。

- finder -- 查找器

  一种会尝试查找被导入模块的 [loader](https://docs.python.org/zh-cn/3/glossary.html#term-loader) 的对象。从 Python 3.3 起存在两种类型的查找器: [元路径查找器](https://docs.python.org/zh-cn/3/glossary.html#term-meta-path-finder) 配合 [`sys.meta_path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.meta_path) 使用，以及 [path entry finders](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder) 配合 [`sys.path_hooks`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_hooks) 使用。更多详情可参见 [**PEP 302**](https://www.python.org/dev/peps/pep-0302), [**PEP 420**](https://www.python.org/dev/peps/pep-0420) 和 [**PEP 451**](https://www.python.org/dev/peps/pep-0451)。

- floor division -- 向下取整除法

  向下舍入到最接近的整数的数学除法。向下取整除法的运算符是 `//` 。例如，表达式 `11 // 4` 的计算结果是 `2` ，而与之相反的是浮点数的真正除法返回 `2.75` 。注意 `(-11) // 4` 会返回 `-3` 因为这是 `-2.75` *向下* 舍入得到的结果。见 [**PEP 238**](https://www.python.org/dev/peps/pep-0238) 。

- function -- 函数

  可以向调用者返回某个值的一组语句。还可以向其传入零个或多个 [参数](https://docs.python.org/zh-cn/3/glossary.html#term-argument) 并在函数体执行中被使用。另见 [parameter](https://docs.python.org/zh-cn/3/glossary.html#term-parameter), [method](https://docs.python.org/zh-cn/3/glossary.html#term-method) 和 [函数定义](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#function) 等节。

- function annotation -- 函数注解

  即针对函数形参或返回值的 [annotation](https://docs.python.org/zh-cn/3/glossary.html#term-annotation) 。函数标注通常用于 [类型提示](https://docs.python.org/zh-cn/3/glossary.html#term-type-hint)：例如以下函数预期接受两个 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 参数并预期返回一个 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 值:`def sum_two_numbers(a: int, b: int) -> int:   return a + b `函数标注语法的详解见 [函数定义](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#function) 一节。请参看 [variable annotation](https://docs.python.org/zh-cn/3/glossary.html#term-variable-annotation) 和 [**PEP 484**](https://www.python.org/dev/peps/pep-0484) 对此功能的描述。

- __future__

  一种伪模块，可被程序员用来启用与当前解释器不兼容的新语言特性。通过导入 [`__future__`](https://docs.python.org/zh-cn/3/library/__future__.html#module-__future__) 模块并对其中的变量求值，你可以查看新特性何时首次加入语言以及何时成为默认:>>>`>>> import __future__ >>> __future__.division _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 8192) `

- garbage collection -- 垃圾回收

  释放不再被使用的内存空间的过程。Python 是通过引用计数和一个能够检测和打破循环引用的循环垃圾回收器来执行垃圾回收的。可以使用 [`gc`](https://docs.python.org/zh-cn/3/library/gc.html#module-gc) 模块来控制垃圾回收器。

- generator -- 生成器

  返回一个 [generator iterator](https://docs.python.org/zh-cn/3/glossary.html#term-generator-iterator) 的函数。它看起来很像普通函数，不同点在于其包含 [`yield`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#yield) 表达式以便产生一系列值供给 for-循环使用或是通过 [`next()`](https://docs.python.org/zh-cn/3/library/functions.html#next) 函数逐一获取。通常是指生成器函数，但在某些情况下也可能是指 *生成器迭代器*。如果需要清楚表达具体含义，请使用全称以避免歧义。

- generator iterator -- 生成器迭代器

  [generator](https://docs.python.org/zh-cn/3/glossary.html#term-generator) 函数所创建的对象。每个 [`yield`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#yield) 会临时暂停处理，记住当前位置执行状态（包括局部变量和挂起的 try 语句）。当该 *生成器迭代器* 恢复时，它会从离开位置继续执行（这与每次调用都从新开始的普通函数差别很大）。

- generator expression -- 生成器表达式

  返回一个迭代器的表达式。 它看起来很像普通表达式后面带有定义了一个循环变量、范围的 `for` 子句，以及一个可选的 `if` 子句。 以下复合表达式会为外层函数生成一系列值:>>>`>>> sum(i*i for i in range(10))         # sum of squares 0, 1, 4, ... 81 285 `

- generic function -- 泛型函数

  为不同的类型实现相同操作的多个函数所组成的函数。在调用时会由调度算法来确定应该使用哪个实现。另请参见 [single dispatch](https://docs.python.org/zh-cn/3/glossary.html#term-single-dispatch) 术语表条目、[`functools.singledispatch()`](https://docs.python.org/zh-cn/3/library/functools.html#functools.singledispatch) 装饰器以及 [**PEP 443**](https://www.python.org/dev/peps/pep-0443)。

- GIL

  参见 [global interpreter lock](https://docs.python.org/zh-cn/3/glossary.html#term-global-interpreter-lock)。

- global interpreter lock -- 全局解释器锁

  [CPython](https://docs.python.org/zh-cn/3/glossary.html#term-cpython) 解释器所采用的一种机制，它确保同一时刻只有一个线程在执行 Python [bytecode](https://docs.python.org/zh-cn/3/glossary.html#term-bytecode)。此机制通过设置对象模型（包括 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 等重要内置类型）针对并发访问的隐式安全简化了 CPython 实现。给整个解释器加锁使得解释器多线程运行更方便，其代价则是牺牲了在多处理器上的并行性。不过，某些标准库或第三方库的扩展模块被设计为在执行计算密集型任务如压缩或哈希时释放 GIL。此外，在执行 I/O 操作时也总是会释放 GIL。创建一个（以更精细粒度来锁定共享数据的）“自由线程”解释器的努力从未获得成功，因为这会牺牲在普通单处理器情况下的性能。据信克服这种性能问题的措施将导致实现变得更复杂，从而更难以维护。

- hash-based pyc -- 基于哈希的 pyc

  使用对应源文件的哈希值而非最后修改时间来确定其有效性的字节码缓存文件。 参见 [已缓存字节码的失效](https://docs.python.org/zh-cn/3/reference/import.html#pyc-invalidation)。

- hashable -- 可哈希

  一个对象的哈希值如果在其生命周期内绝不改变，就被称为 *可哈希* （它需要具有 [`__hash__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__hash__) 方法），并可以同其他对象进行比较（它需要具有 [`__eq__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__eq__) 方法）。可哈希对象必须具有相同的哈希值比较结果才会相同。可哈希性使得对象能够作为字典键或集合成员使用，因为这些数据结构要在内部使用哈希值。大多数 Python 中的不可变内置对象都是可哈希的；可变容器（例如列表或字典）都不可哈希；不可变容器（例如元组和 frozenset）仅当它们的元素均为可哈希时才是可哈希的。 用户定义类的实例对象默认是可哈希的。 它们在比较时一定不相同（除非是与自己比较），它们的哈希值的生成是基于它们的 [`id()`](https://docs.python.org/zh-cn/3/library/functions.html#id)。

- IDLE

  Python 的 IDE，“集成开发与学习环境”的英文缩写。是 Python 标准发行版附带的基本编程器和解释器环境。

- immutable -- 不可变

  具有固定值的对象。不可变对象包括数字、字符串和元组。这样的对象不能被改变。如果必须存储一个不同的值，则必须创建新的对象。它们在需要常量哈希值的地方起着重要作用，例如作为字典中的键。

- import path -- 导入路径

  由多个位置（或 [路径条目](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry)）组成的列表，会被模块的 [path based finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-based-finder) 用来查找导入目标。在导入时，此位置列表通常来自 [`sys.path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path)，但对次级包来说也可能来自上级包的 `__path__` 属性。

- importing -- 导入

  令一个模块中的 Python 代码能为另一个模块中的 Python 代码所使用的过程。

- importer -- 导入器

  查找并加载模块的对象；此对象既属于 [finder](https://docs.python.org/zh-cn/3/glossary.html#term-finder) 又属于 [loader](https://docs.python.org/zh-cn/3/glossary.html#term-loader)。

- interactive -- 交互

  Python 带有一个交互式解释器，即你可以在解释器提示符后输入语句和表达式，立即执行并查看其结果。只需不带参数地启动 `python` 命令（也可以在你的计算机开始菜单中选择相应菜单项）。在测试新想法或检验模块和包的时候用这种方式会非常方便（请记得使用 `help(x)`）。

- interpreted -- 解释型

  Python 一是种解释型语言，与之相对的是编译型语言，虽然两者的区别由于字节码编译器的存在而会有所模糊。这意味着源文件可以直接运行而不必显式地创建可执行文件再运行。解释型语言通常具有比编译型语言更短的开发/调试周期，但是其程序往往运行得更慢。参见 [interactive](https://docs.python.org/zh-cn/3/glossary.html#term-interactive)。

- interpreter shutdown -- 解释器关闭

  当被要求关闭时，Python 解释器将进入一个特殊运行阶段并逐步释放所有已分配资源，例如模块和各种关键内部结构等。它还会多次调用 [垃圾回收器](https://docs.python.org/zh-cn/3/glossary.html#term-garbage-collection)。这会触发用户定义析构器或弱引用回调中的代码执行。在关闭阶段执行的代码可能会遇到各种异常，因为其所依赖的资源已不再有效（常见的例子有库模块或警告机制等）。解释器需要关闭的主要原因有 `__main__` 模块或所运行的脚本已完成执行。

- iterable -- 可迭代对象

  能够逐一返回其成员项的对象。可迭代对象的例子包括所有序列类型（例如 [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list)、[`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 和 [`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple)）以及某些非序列类型例如 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict)、[文件对象](https://docs.python.org/zh-cn/3/glossary.html#term-file-object) 以及定义了 [`__iter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 方法或是实现了 [Sequence](https://docs.python.org/zh-cn/3/glossary.html#term-sequence) 语义的 [`__getitem__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getitem__) 方法的任意自定义类对象。可迭代对象被可用于 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 循环以及许多其他需要一个序列的地方（[`zip()`](https://docs.python.org/zh-cn/3/library/functions.html#zip)、[`map()`](https://docs.python.org/zh-cn/3/library/functions.html#map) ...）。当一个可迭代对象作为参数传给内置函数 [`iter()`](https://docs.python.org/zh-cn/3/library/functions.html#iter) 时，它会返回该对象的迭代器。这种迭代器适用于对值集合的一次性遍历。在使用可迭代对象时，你通常不需要调用 [`iter()`](https://docs.python.org/zh-cn/3/library/functions.html#iter) 或者自己处理迭代器对象。`for` 语句会为你自动处理那些操作，创建一个临时的未命名变量用来在循环期间保存迭代器。参见 [iterator](https://docs.python.org/zh-cn/3/glossary.html#term-iterator)、[sequence](https://docs.python.org/zh-cn/3/glossary.html#term-sequence) 以及 [generator](https://docs.python.org/zh-cn/3/glossary.html#term-generator)。

- iterator -- 迭代器

  用来表示一连串数据流的对象。重复调用迭代器的 [`__next__()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#iterator.__next__) 方法（或将其传给内置函数 [`next()`](https://docs.python.org/zh-cn/3/library/functions.html#next)）将逐个返回流中的项。当没有数据可用时则将引发 [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration) 异常。到这时迭代器对象中的数据项已耗尽，继续调用其 `__next__()` 方法只会再次引发 [`StopIteration`](https://docs.python.org/zh-cn/3/library/exceptions.html#StopIteration) 异常。迭代器必须具有 [`__iter__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__iter__) 方法用来返回该迭代器对象自身，因此迭代器必定也是可迭代对象，可被用于其他可迭代对象适用的大部分场合。一个显著的例外是那些会多次重复访问迭代项的代码。容器对象（例如 [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list)）在你每次向其传入 [`iter()`](https://docs.python.org/zh-cn/3/library/functions.html#iter) 函数或是在 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 循环中使用它时都会产生一个新的迭代器。如果在此情况下你尝试用迭代器则会返回在之前迭代过程中被耗尽的同一迭代器对象，使其看起来就像是一个空容器。更多信息可查看 [迭代器类型](https://docs.python.org/zh-cn/3/library/stdtypes.html#typeiter)。

- key function -- 键函数

  键函数或称整理函数，是能够返回用于排序或排位的值的可调用对象。例如，[`locale.strxfrm()`](https://docs.python.org/zh-cn/3/library/locale.html#locale.strxfrm) 可用于生成一个符合特定区域排序约定的排序键。Python 中有许多工具都允许用键函数来控制元素的排位或分组方式。其中包括 [`min()`](https://docs.python.org/zh-cn/3/library/functions.html#min), [`max()`](https://docs.python.org/zh-cn/3/library/functions.html#max), [`sorted()`](https://docs.python.org/zh-cn/3/library/functions.html#sorted), [`list.sort()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list.sort), [`heapq.merge()`](https://docs.python.org/zh-cn/3/library/heapq.html#heapq.merge), [`heapq.nsmallest()`](https://docs.python.org/zh-cn/3/library/heapq.html#heapq.nsmallest), [`heapq.nlargest()`](https://docs.python.org/zh-cn/3/library/heapq.html#heapq.nlargest) 以及 [`itertools.groupby()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.groupby)。要创建一个键函数有多种方式。例如，[`str.lower()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str.lower) 方法可以用作忽略大小写排序的键函数。另外，键函数也可通过 [`lambda`](https://docs.python.org/zh-cn/3/reference/expressions.html#lambda) 表达式来创建，例如 `lambda r: (r[0], r[2])`。还有 [`operator`](https://docs.python.org/zh-cn/3/library/operator.html#module-operator) 模块提供了三个键函数构造器：[`attrgetter()`](https://docs.python.org/zh-cn/3/library/operator.html#operator.attrgetter)、[`itemgetter()`](https://docs.python.org/zh-cn/3/library/operator.html#operator.itemgetter) 和 [`methodcaller()`](https://docs.python.org/zh-cn/3/library/operator.html#operator.methodcaller)。请查看 [如何排序](https://docs.python.org/zh-cn/3/howto/sorting.html#sortinghowto) 一节以获取创建和使用键函数的示例。

- keyword argument -- 关键字参数

  参见 [argument](https://docs.python.org/zh-cn/3/glossary.html#term-argument)。

- lambda

  由一个单独 [expression](https://docs.python.org/zh-cn/3/glossary.html#term-expression) 构成的匿名内联函数，表达式会在调用时被求值。创建 lambda 函数的句法为 `lambda [parameters]: expression`

- LBYL

  “先查看后跳跃”的英文缩写。这种代码编写风格会在进行调用或查找之前显式地检查前提条件。此风格与 [EAFP](https://docs.python.org/zh-cn/3/glossary.html#term-eafp) 方式恰成对比，其特点是大量使用 [`if`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#if) 语句。在多线程环境中，LBYL 方式会导致“查看”和“跳跃”之间发生条件竞争风险。例如，以下代码 `if key in mapping: return mapping[key]` 可能由于在检查操作之后其他线程从 *mapping* 中移除了 *key* 而出错。这种问题可通过加锁或使用 EAFP 方式来解决。

- list -- 列表

  Python 内置的一种 [sequence](https://docs.python.org/zh-cn/3/glossary.html#term-sequence)。虽然名为列表，但更类似于其他语言中的数组而非链接列表，因为访问元素的时间复杂度为 O(1)。

- list comprehension -- 列表推导式

  处理一个序列中的所有或部分元素并返回结果列表的一种紧凑写法。`result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0]` 将生成一个 0 到 255 范围内的十六进制偶数对应字符串（0x..）的列表。其中 [`if`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#if) 子句是可选的，如果省略则 `range(256)` 中的所有元素都会被处理。

- loader -- 加载器

  负责加载模块的对象。它必须定义名为 `load_module()` 的方法。加载器通常由一个 [finder](https://docs.python.org/zh-cn/3/glossary.html#term-finder) 返回。详情参见 [**PEP 302**](https://www.python.org/dev/peps/pep-0302)，对于 [abstract base class](https://docs.python.org/zh-cn/3/glossary.html#term-abstract-base-class) 可参见 [`importlib.abc.Loader`](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.Loader)。

- magic method -- 魔术方法

  [special method](https://docs.python.org/zh-cn/3/glossary.html#term-special-method) 的非正式同义词 。

- mapping -- 映射

  一种支持任意键查找并实现了 [`Mapping`](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Mapping) 或 [`MutableMapping`](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.MutableMapping) [抽象基类](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections-abstract-base-classes) 中所规定方法的容器对象。 此类对象的例子包括 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict), [`collections.defaultdict`](https://docs.python.org/zh-cn/3/library/collections.html#collections.defaultdict), [`collections.OrderedDict`](https://docs.python.org/zh-cn/3/library/collections.html#collections.OrderedDict) 以及 [`collections.Counter`](https://docs.python.org/zh-cn/3/library/collections.html#collections.Counter)。

- meta path finder -- 元路径查找器

  [`sys.meta_path`](https://docs.python.org/zh-cn/3/library/sys.html#sys.meta_path) 的搜索所返回的 [finder](https://docs.python.org/zh-cn/3/glossary.html#term-finder)。元路径查找器与 [path entry finders](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder) 存在关联但并不相同。请查看 [`importlib.abc.MetaPathFinder`](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.MetaPathFinder) 了解元路径查找器所实现的方法。

- metaclass -- 元类

  一种用于创建类的类。类定义包含类名、类字典和基类列表。元类负责接受上述三个参数并创建相应的类。大部分面向对象的编程语言都会提供一个默认实现。Python 的特别之处在于可以创建自定义元类。大部分用户永远不需要这个工具，但当需要出现时，元类可提供强大而优雅的解决方案。它们已被用于记录属性访问日志、添加线程安全性、跟踪对象创建、实现单例，以及其他许多任务。更多详情参见 [元类](https://docs.python.org/zh-cn/3/reference/datamodel.html#metaclasses)。

- method -- 方法

  在类内部定义的函数。如果作为该类的实例的一个属性来调用，方法将会获取实例对象作为其第一个 [argument](https://docs.python.org/zh-cn/3/glossary.html#term-argument) (通常命名为 `self`)。参见 [function](https://docs.python.org/zh-cn/3/glossary.html#term-function) 和 [nested scope](https://docs.python.org/zh-cn/3/glossary.html#term-nested-scope)。

- method resolution order -- 方法解析顺序

  方法解析顺序就是在查找成员时搜索全部基类所用的先后顺序。请查看 [Python 2.3 方法解析顺序](https://www.python.org/download/releases/2.3/mro/) 了解自 2.3 版起 Python 解析器所用相关算法的详情。

- module -- 模块

  此对象是 Python 代码的一种组织单位。各模块具有独立的命名空间，可包含任意 Python 对象。模块可通过 [importing](https://docs.python.org/zh-cn/3/glossary.html#term-importing) 操作被加载到 Python 中。另见 [package](https://docs.python.org/zh-cn/3/glossary.html#term-package)。

- module spec -- 模块规格

  一个命名空间，其中包含用于加载模块的相关导入信息。是 [`importlib.machinery.ModuleSpec`](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.machinery.ModuleSpec) 的实例。

- MRO

  参见 [method resolution order](https://docs.python.org/zh-cn/3/glossary.html#term-method-resolution-order)。

- mutable -- 可变

  可变对象可以在其 [`id()`](https://docs.python.org/zh-cn/3/library/functions.html#id) 保持固定的情况下改变其取值。另请参见 [immutable](https://docs.python.org/zh-cn/3/glossary.html#term-immutable)。

- named tuple -- 具名元组

  术语“具名元组”可用于任何继承自元组，并且其中的可索引元素还能使用名称属性来访问的类型或类。 这样的类型或类还可能拥有其他特性。有些内置类型属于具名元组，包括 [`time.localtime()`](https://docs.python.org/zh-cn/3/library/time.html#time.localtime) 和 [`os.stat()`](https://docs.python.org/zh-cn/3/library/os.html#os.stat) 的返回值。 另一个例子是 [`sys.float_info`](https://docs.python.org/zh-cn/3/library/sys.html#sys.float_info):>>>`>>> sys.float_info[1]                   # indexed access 1024 >>> sys.float_info.max_exp              # named field access 1024 >>> isinstance(sys.float_info, tuple)   # kind of tuple True `有些具名元组是内置类型（例如上面的例子）。 此外，具名元组还可通过常规类定义从 [`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple) 继承并定义名称字段的方式来创建。 这样的类可以手工编写，或者使用工厂函数 [`collections.namedtuple()`](https://docs.python.org/zh-cn/3/library/collections.html#collections.namedtuple) 创建。 后一种方式还会添加一些手工编写或内置具名元组所没有的额外方法。

- namespace -- 命名空间

  命名空间是存放变量的场所。命名空间有局部、全局和内置的，还有对象中的嵌套命名空间（在方法之内）。命名空间通过防止命名冲突来支持模块化。例如，函数 [`builtins.open`](https://docs.python.org/zh-cn/3/library/functions.html#open) 与 [`os.open()`](https://docs.python.org/zh-cn/3/library/os.html#os.open) 可通过各自的命名空间来区分。命名空间还通过明确哪个模块实现那个函数来帮助提高可读性和可维护性。例如，[`random.seed()`](https://docs.python.org/zh-cn/3/library/random.html#random.seed) 或 [`itertools.islice()`](https://docs.python.org/zh-cn/3/library/itertools.html#itertools.islice) 这种写法明确了这些函数是由 [`random`](https://docs.python.org/zh-cn/3/library/random.html#module-random) 与 [`itertools`](https://docs.python.org/zh-cn/3/library/itertools.html#module-itertools) 模块分别实现的。

- namespace package -- 命名空间包

  [**PEP 420**](https://www.python.org/dev/peps/pep-0420) 所引入的一种仅被用作子包的容器的 [package](https://docs.python.org/zh-cn/3/glossary.html#term-package)，命名空间包可以没有实体表示物，其描述方式与 [regular package](https://docs.python.org/zh-cn/3/glossary.html#term-regular-package) 不同，因为它们没有 `__init__.py` 文件。另可参见 [module](https://docs.python.org/zh-cn/3/glossary.html#term-module)。

- nested scope -- 嵌套作用域

  在一个定义范围内引用变量的能力。例如，在另一函数之内定义的函数可以引用前者的变量。请注意嵌套作用域默认只对引用有效而对赋值无效。局部变量的读写都受限于最内层作用域。类似的，全局变量的读写则作用于全局命名空间。通过 [`nonlocal`](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#nonlocal) 关键字可允许写入外层作用域。

- new-style class -- 新式类

  对于目前已被应于所有类对象的类形式的旧称谓。在早先的 Python 版本中，只有新式类能够使用 Python 新增的更灵活特性，例如 [`__slots__`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__slots__)、描述符、特征属性、[`__getattribute__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getattribute__)、类方法和静态方法等。

- object -- 对象

  任何具有状态（属性或值）以及预定义行为（方法）的数据。object 也是任何 [new-style class](https://docs.python.org/zh-cn/3/glossary.html#term-new-style-class) 的最顶层基类名。

- package -- 包

  一种可包含子模块或递归地包含子包的 Python [module](https://docs.python.org/zh-cn/3/glossary.html#term-module)。从技术上说，包是带有 `__path__` 属性的 Python 模块。另参见 [regular package](https://docs.python.org/zh-cn/3/glossary.html#term-regular-package) 和 [namespace package](https://docs.python.org/zh-cn/3/glossary.html#term-namespace-package)。

- parameter -- 形参

  [function](https://docs.python.org/zh-cn/3/glossary.html#term-function) （或方法）定义中的命名实体，它指定函数可以接受的一个 [argument](https://docs.python.org/zh-cn/3/glossary.html#term-argument) （或在某些情况下，多个实参）。有五种形参：*positional-or-keyword*：位置或关键字，指定一个可以作为 [位置参数](https://docs.python.org/zh-cn/3/glossary.html#term-argument) 传入也可以作为 [关键字参数](https://docs.python.org/zh-cn/3/glossary.html#term-argument) 传入的实参。这是默认的形参类型，例如下面的 *foo* 和 *bar*:`def func(foo, bar=None): ... `*positional-only*：仅限位置，指定一个只能按位置传入的参数。Python 中没有定义仅限位置形参的语法。但是一些内置函数有仅限位置形参（比如 [`abs()`](https://docs.python.org/zh-cn/3/library/functions.html#abs)）。*keyword-only*：仅限关键字，指定一个只能通过关键字传入的参数。仅限关键字形参可通过在函数定义的形参列表中包含单个可变位置形参或者在多个可变位置形参之前放一个 `*` 来定义，例如下面的 *kw_only1* 和 *kw_only2*:`def func(arg, *, kw_only1, kw_only2): ... `*var-positional*：可变位置，指定可以提供由一个任意数量的位置参数构成的序列（附加在其他形参已接受的位置参数之后）。这种形参可通过在形参名称前加缀 `*` 来定义，例如下面的 *args*:`def func(*args, **kwargs): ... `*var-keyword*：可变关键字，指定可以提供任意数量的关键字参数（附加在其他形参已接受的关键字参数之后）。这种形参可通过在形参名称前加缀 `**` 来定义，例如上面的 *kwargs*。形参可以同时指定可选和必选参数，也可以为某些可选参数指定默认值。另参见 [argument](https://docs.python.org/zh-cn/3/glossary.html#term-argument) 术语表条目、[参数与形参的区别](https://docs.python.org/zh-cn/3/faq/programming.html#faq-argument-vs-parameter) 中的常见问题、[`inspect.Parameter`](https://docs.python.org/zh-cn/3/library/inspect.html#inspect.Parameter) 类、[函数定义](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#function) 一节以及 [**PEP 362**](https://www.python.org/dev/peps/pep-0362)。

- path entry -- 路径入口

  [import path](https://docs.python.org/zh-cn/3/glossary.html#term-import-path) 中的一个单独位置，会被 [path based finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-based-finder) 用来查找要导入的模块。

- path entry finder -- 路径入口查找器

  任一可调用对象使用 [`sys.path_hooks`](https://docs.python.org/zh-cn/3/library/sys.html#sys.path_hooks) (即 [path entry hook](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-hook)) 返回的 [finder](https://docs.python.org/zh-cn/3/glossary.html#term-finder)，此种对象能通过 [path entry](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry) 来定位模块。请参看 [`importlib.abc.PathEntryFinder`](https://docs.python.org/zh-cn/3/library/importlib.html#importlib.abc.PathEntryFinder) 以了解路径入口查找器所实现的各个方法。

- path entry hook -- 路径入口钩子

  一种可调用对象，在知道如何查找特定 [path entry](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry) 中的模块的情况下能够使用 `sys.path_hook` 列表返回一个 [path entry finder](https://docs.python.org/zh-cn/3/glossary.html#term-path-entry-finder)。

- path based finder -- 基于路径的查找器

  默认的一种 [元路径查找器](https://docs.python.org/zh-cn/3/glossary.html#term-meta-path-finder)，可在一个 [import path](https://docs.python.org/zh-cn/3/glossary.html#term-import-path) 中查找模块。

- path-like object -- 路径类对象

  代表一个文件系统路径的对象。类路径对象可以是一个表示路径的 [`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 或者 [`bytes`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes) 对象，还可以是一个实现了 [`os.PathLike`](https://docs.python.org/zh-cn/3/library/os.html#os.PathLike) 协议的对象。一个支持 [`os.PathLike`](https://docs.python.org/zh-cn/3/library/os.html#os.PathLike) 协议的对象可通过调用 [`os.fspath()`](https://docs.python.org/zh-cn/3/library/os.html#os.fspath) 函数转换为 [`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 或者 [`bytes`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes) 类型的文件系统路径；[`os.fsdecode()`](https://docs.python.org/zh-cn/3/library/os.html#os.fsdecode) 和 [`os.fsencode()`](https://docs.python.org/zh-cn/3/library/os.html#os.fsencode) 可被分别用来确保获得 [`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 或 [`bytes`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes) 类型的结果。此对象是由 [**PEP 519**](https://www.python.org/dev/peps/pep-0519) 引入的。

- PEP

  “Python 增强提议”的英文缩写。一个 PEP 就是一份设计文档，用来向 Python 社区提供信息，或描述一个 Python 的新增特性及其进度或环境。PEP 应当提供精确的技术规格和所提议特性的原理说明。PEP 应被作为提出主要新特性建议、收集社区对特定问题反馈以及为必须加入 Python 的设计决策编写文档的首选机制。PEP 的作者有责任在社区内部建立共识，并应将不同意见也记入文档。参见 [**PEP 1**](https://www.python.org/dev/peps/pep-0001)。

- portion -- 部分

  构成一个命名空间包的单个目录内文件集合（也可能存放于一个 zip 文件内），具体定义见 [**PEP 420**](https://www.python.org/dev/peps/pep-0420)。

- positional argument -- 位置参数

  参见 [argument](https://docs.python.org/zh-cn/3/glossary.html#term-argument)。

- provisional API -- 暂定 API

  暂定 API 是指被有意排除在标准库的向后兼容性保证之外的应用编程接口。虽然此类接口通常不会再有重大改变，但只要其被标记为暂定，就可能在核心开发者确定有必要的情况下进行向后不兼容的更改（甚至包括移除该接口）。此种更改并不会随意进行 -- 仅在 API 被加入之前未考虑到的严重基础性缺陷被发现时才可能会这样做。即便是对暂定 API 来说，向后不兼容的更改也会被视为“最后的解决方案” —— 任何问题被确认时都会尽可能先尝试找到一种向后兼容的解决方案。这种处理过程允许标准库持续不断地演进，不至于被有问题的长期性设计缺陷所困。详情见 [**PEP 411**](https://www.python.org/dev/peps/pep-0411)。

- provisional package -- 暂定包

  参见 [provisional API](https://docs.python.org/zh-cn/3/glossary.html#term-provisional-api)。

- Python 3000

  Python 3.x 发布路线的昵称（这个名字在版本 3 的发布还遥遥无期的时候就已出现了）。有时也被缩写为“Py3k”。

- Pythonic

  指一个思路或一段代码紧密遵循了 Python 语言最常用的风格和理念，而不是使用其他语言中通用的概念来实现代码。例如，Python 的常用风格是使用 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for) 语句循环来遍历一个可迭代对象中的所有元素。许多其他语言没有这样的结构，因此不熟悉 Python 的人有时会选择使用一个数字计数器:`for i in range(len(food)):    print(food[i]) `而相应的更简洁更 Pythonic 的方法是这样的:`for piece in food:    print(piece) `

- qualified name -- 限定名称

  一个以点号分隔的名称，显示从模块的全局作用域到该模块中定义的某个类、函数或方法的“路径”，相关定义见 [**PEP 3155**](https://www.python.org/dev/peps/pep-3155)。对于最高层级的函数和类，限定名称与对象名称一致:>>>`>>> class C: ...     class D: ...         def meth(self): ...             pass ... >>> C.__qualname__ 'C' >>> C.D.__qualname__ 'C.D' >>> C.D.meth.__qualname__ 'C.D.meth' `当被用于引用模块时，*完整限定名称* 意为标示该模块的以点号分隔的整个路径，其中包含其所有的父包，例如 `email.mime.text`:>>>`>>> import email.mime.text >>> email.mime.text.__name__ 'email.mime.text' `

- reference count -- 引用计数

  对特定对象的引用的数量。当一个对象的引用计数降为零时，所分配资源将被释放。引用计数对 Python 代码来说通常是不可见的，但它是 [CPython](https://docs.python.org/zh-cn/3/glossary.html#term-cpython) 实现的一个关键元素。[`sys`](https://docs.python.org/zh-cn/3/library/sys.html#module-sys) 模块定义了一个 [`getrefcount()`](https://docs.python.org/zh-cn/3/library/sys.html#sys.getrefcount) 函数，程序员可调用它来返回特定对象的引用计数。

- regular package -- 常规包

  传统型的 [package](https://docs.python.org/zh-cn/3/glossary.html#term-package)，例如包含有一个 `__init__.py` 文件的目录。另参见 [namespace package](https://docs.python.org/zh-cn/3/glossary.html#term-namespace-package)。

- __slots__

  一种写在类内部的声明，通过预先声明实例属性等对象并移除实例字典来节省内存。虽然这种技巧很流行，但想要用好却并不容易，最好是只保留在少数情况下采用，例如极耗内存的应用程序，并且其中包含大量实例。

- sequence -- 序列

  一种 [iterable](https://docs.python.org/zh-cn/3/glossary.html#term-iterable)，它支持通过 [`__getitem__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getitem__) 特殊方法来使用整数索引进行高效的元素访问，并定义了一个返回序列长度的 [`__len__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__len__) 方法。内置的序列类型有 [`list`](https://docs.python.org/zh-cn/3/library/stdtypes.html#list)、[`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str)、[`tuple`](https://docs.python.org/zh-cn/3/library/stdtypes.html#tuple) 和 [`bytes`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes)。注意虽然 [`dict`](https://docs.python.org/zh-cn/3/library/stdtypes.html#dict) 也支持 [`__getitem__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getitem__) 和 [`__len__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__len__)，但它被认为属于映射而非序列，因为它查找时使用任意的 [immutable](https://docs.python.org/zh-cn/3/glossary.html#term-immutable) 键而非整数。[`collections.abc.Sequence`](https://docs.python.org/zh-cn/3/library/collections.abc.html#collections.abc.Sequence) 抽象基类定义了一个更丰富的接口，它超越了 [`__getitem__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__getitem__) 和 [`__len__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__len__)，添加了 `count()`, `index()`, [`__contains__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__contains__) 和 [`__reversed__()`](https://docs.python.org/zh-cn/3/reference/datamodel.html#object.__reversed__) 。 可以使用 `register()` 显式注册实现此扩展接口的类型。

- single dispatch -- 单分派

  一种 [generic function](https://docs.python.org/zh-cn/3/glossary.html#term-generic-function) 分派形式，其实现是基于单个参数的类型来选择的。

- slice -- 切片

  通常只包含了特定 [sequence](https://docs.python.org/zh-cn/3/glossary.html#term-sequence) 的一部分的对象。切片是通过使用下标标记来创建的，在 `[]` 中给出几个以冒号分隔的数字，例如 `variable_name[1:3:5]`。方括号（下标）标记在内部使用 [`slice`](https://docs.python.org/zh-cn/3/library/functions.html#slice) 对象。

- special method -- 特殊方法

  一种由 Python 隐式调用的方法，用来对某个类型执行特定操作例如相加等等。这种方法的名称的首尾都为双下划线。特殊方法的文档参见 [特殊方法名称](https://docs.python.org/zh-cn/3/reference/datamodel.html#specialnames)。

- statement -- 语句

  语句是程序段（一个代码“块”）的组成单位。一条语句可以是一个 [expression](https://docs.python.org/zh-cn/3/glossary.html#term-expression) 或某个带有关键字的结构，例如 [`if`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#if)、[`while`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#while) 或 [`for`](https://docs.python.org/zh-cn/3/reference/compound_stmts.html#for)。

- text encoding -- 文本编码

  用于将Unicode字符串编码为字节串的编码器。

- text file -- 文本文件

  一种能够读写 [`str`](https://docs.python.org/zh-cn/3/library/stdtypes.html#str) 对象的 [file object](https://docs.python.org/zh-cn/3/glossary.html#term-file-object)。通常一个文本文件实际是访问一个面向字节的数据流并自动处理 [text encoding](https://docs.python.org/zh-cn/3/glossary.html#term-text-encoding)。文本文件的例子包括以文本模式（`'r'` 或 `'w'`）打开的文件、[`sys.stdin`](https://docs.python.org/zh-cn/3/library/sys.html#sys.stdin)、[`sys.stdout`](https://docs.python.org/zh-cn/3/library/sys.html#sys.stdout) 以及 [`io.StringIO`](https://docs.python.org/zh-cn/3/library/io.html#io.StringIO) 的实例。另请参看 [binary file](https://docs.python.org/zh-cn/3/glossary.html#term-binary-file) 了解能够读写 [字节类对象](https://docs.python.org/zh-cn/3/glossary.html#term-bytes-like-object) 的文件对象。

- triple-quoted string -- 三引号字符串

  首尾各带三个连续双引号（"）或者单引号（'）的字符串。它们在功能上与首尾各用一个引号标注的字符串没有什么不同，但是有多种用处。它们允许你在字符串内包含未经转义的单引号和双引号，并且可以跨越多行而无需使用连接符，在编写文档字符串时特别好用。

- type -- 类型

  类型决定一个 Python 对象属于什么种类；每个对象都具有一种类型。要知道对象的类型，可以访问它的 [`__class__`](https://docs.python.org/zh-cn/3/library/stdtypes.html#instance.__class__) 属性，或是通过 `type(obj)` 来获取。

- type alias -- 类型别名

  一个类型的同义词，创建方式是把类型赋值给特定的标识符。类型别名的作用是简化 [类型提示](https://docs.python.org/zh-cn/3/glossary.html#term-type-hint)。例如:`from typing import List, Tuple def remove_gray_shades(        colors: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:    pass `可以这样提高可读性:`from typing import List, Tuple Color = Tuple[int, int, int] def remove_gray_shades(colors: List[Color]) -> List[Color]:    pass `参见 [`typing`](https://docs.python.org/zh-cn/3/library/typing.html#module-typing) 和 [**PEP 484**](https://www.python.org/dev/peps/pep-0484)，其中有对此功能的详细描述。

- type hint -- 类型提示

  [annotation](https://docs.python.org/zh-cn/3/glossary.html#term-annotation) 为变量、类属性、函数的形参或返回值指定预期的类型。类型提示属于可选项，Python 不要求提供，但其可对静态类型分析工具起作用，并可协助 IDE 实现代码补全与重构。全局变量、类属性和函数的类型提示可以使用 [`typing.get_type_hints()`](https://docs.python.org/zh-cn/3/library/typing.html#typing.get_type_hints) 来访问，但局部变量则不可以。参见 [`typing`](https://docs.python.org/zh-cn/3/library/typing.html#module-typing) 和 [**PEP 484**](https://www.python.org/dev/peps/pep-0484)，其中有对此功能的详细描述。

- universal newlines -- 通用换行

  一种解读文本流的方式，将以下所有符号都识别为行结束标志：Unix 的行结束约定 `'\n'`、Windows 的约定 `'\r\n'` 以及旧版 Macintosh 的约定 `'\r'`。参见 [**PEP 278**](https://www.python.org/dev/peps/pep-0278) 和 [**PEP 3116**](https://www.python.org/dev/peps/pep-3116) 和 [`bytes.splitlines()`](https://docs.python.org/zh-cn/3/library/stdtypes.html#bytes.splitlines) 了解更多用法说明。

- variable annotation -- 变量注解

  对变量或类属性的 [annotation](https://docs.python.org/zh-cn/3/glossary.html#term-annotation)。在标注变量或类属性时，还可选择为其赋值:`class C:    field: 'annotation' `变量标注通常被用作 [类型提示](https://docs.python.org/zh-cn/3/glossary.html#term-type-hint)：例如以下变量预期接受 [`int`](https://docs.python.org/zh-cn/3/library/functions.html#int) 类型的值:`count: int = 0 `变量标注语法的详细解释见 [带标注的赋值语句](https://docs.python.org/zh-cn/3/reference/simple_stmts.html#annassign) 一节。请参看 [function annotation](https://docs.python.org/zh-cn/3/glossary.html#term-function-annotation)、[**PEP 484**](https://www.python.org/dev/peps/pep-0484) 和 [**PEP 526**](https://www.python.org/dev/peps/pep-0526)，其中对此功能有详细描述。

- virtual environment -- 虚拟环境

  一种采用协作式隔离的运行时环境，允许 Python 用户和应用程序在安装和升级 Python 分发包时不会干扰到同一系统上运行的其他 Python 应用程序的行为。另参见 [`venv`](https://docs.python.org/zh-cn/3/library/venv.html#module-venv)。

- virtual machine -- 虚拟机

  一台完全通过软件定义的计算机。Python 虚拟机可执行字节码编译器所生成的 [bytecode](https://docs.python.org/zh-cn/3/glossary.html#term-bytecode)。

- Zen of Python -- Python 之禅

  列出 Python 设计的原则与哲学，有助于理解与使用这种语言。查看其具体内容可在交互模式提示符中输入 "`import this`"。



