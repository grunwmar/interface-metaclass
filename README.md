# Interface metaclass

*Definig a cell interface ,then defining bacterial, archeal and eukaryotic cells*
```python
from interface import Interface


# Make cell interface
class ICell(metaclass=Interface):
  metabolize: Callable
  replicate:  Callable
  respire:    Callable
  
  cell_membrane: property
  chromosome:    property
```

```python
class Bacterium(ICell):

  def __init__(self):
    self._cell_membrane = "glycerol-ester lipids"
    self._chromosome = "usually one circular"
  
  def metabolize(self): ...
   
  def replicate(self): ...
  
  def respire(self): ...
  
  @property
  def cell_membrane(self):
    return self._cell_membrane
    
  @property
  def chromosome(self):
    return self._chromosome
```

```python
class Archeon(ICell):

  def __init__(self):
    self._cell_membrane = "glycerol-ether lipids"
    self._chromosome = "usually one circular"
  
  def metabolize(self): ...
   
  def replicate(self): ...
  
  def respire(self): ...
  
  @property
  def cell_membrane(self):
    return self._cell_membrane
    
  @property
  def chromosome(self):
    return self._chromosome
```

```python
class Eukaryote(ICell):

  def __init__(self):
    self._cell_membrane = "glycerol-ester lipids"
    self._chromosome = "usually many linear"
  
  def metabolize(self): ...
   
  def replicate(self): ...
  
  def respire(self): ...
  
  @property
  def cell_membrane(self):
    return self._cell_membrane
    
  @property
  def chromosome(self):
    return self._chromosome
```

*There are defined three exceptions*
`InterfaceError`, `NotDefinedInterfaceError`, `InvalidTypeInterfaceError`
