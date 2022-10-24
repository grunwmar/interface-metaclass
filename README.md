# Interface metaclass

## Definition of metaclass
```python
class Interface(type):

  def __interface_check__(mcs):
    undefined_items = {} # Dictionary to keep info about undefined attributes
    invalid_items = {}   # Dictionary to keep info about undefined attributes
    interface_items = mcs.__annotations__ # to get interface definition of required attributes
    
    # block test presence of attributes and then
    # if their values fits to required types.
    # If tests fails, record to undefined_items of invalid_items is made
    for ann, tp in interface_items.items():
      if ann not in dir(mcs):
        undefined_items[ann] = tp
      else:
        m = getattr(mcs, ann)
        if not isinstance(m, tp):
          invalid_items[ann] = (tp, m)

    # if dict undefined_items is not empty, raises NotDefinedInterfaceError
    # with messages which attributes are missing.
    if len(undefined_items) > 0:
      raise NotDefinedInterfaceError(undefined_items)

    # if dict invalid_item is not empty, raises InvalidTypeInterfaceError
    # with messages which attributes have invalid values.
    if len(invalid_items) > 0:
      raise InvalidTypeInterfaceError(invalid_items)
    
    # adds __interface__ attribute to easily access interface requirements e.g. for comparison
    mcs.__interface__ = interface_items 

  # calls constructor of the class, then checked if class has all by interface required attributes
  # and returns instance of the class, or raise exception.
  def __call__(mcs, *args, **kwargs):
    called = super().__call__( *args, **kwargs)
    mcs.__interface_check__()
    return called
    
```

Definig a cell interface, then defining bacterial, archeal and eukaryotic cells
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

There are defined three exceptions `InterfaceError` and its derived `NotDefinedInterfaceError` and `InvalidTypeInterfaceError`. Their detailed description is found in `__doc__` strings in `interface.py`.
