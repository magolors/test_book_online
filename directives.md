---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.6.0
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


# Directives

```{attention}
attention
```

```{caution}
caution
```

```{danger}
danger
```

```{error}
error
```

```{hint}
hint
```

```{important}
important
```

```{note}
note
```

```{seealso}
seealso
```

```{tip}
tip
```

```{warning}
warning
```

```{admonition} tip
:class: tip
admonoition
```

```{code-block} python
A = list(map(int, input().split()))
print(A)
```

```{code-block} cpp
int main(int argc, char *argv[]) {
    return 0;
}
```


```{code-cell} 
a = 3
b = 4
print(a*b)
```

```{code-cell} 
:tags: [remove-output]
!jupyter-book create --help
```

```{code-cell} 
:tags: [remove-input]
!jupyter-book create --help
```

````md
```{directivename} arg1 arg2
:key1: metadata1
:key2: metadata2
My directive content.
```
````

````{toggle}
Some hidden toggle content!

```{admonition} Hidden 
:class: info
このように隠すことができます。
```
````



{fa}`check,text-success mr-1` This is an example of Roles (check mark & success color).

{fa}`check,text-info mr-1` This is an example of Roles (check mark & info color).

