# X-I-A API Tutorial - 01-01: Simple Data Model
## Getting Started

Welcome to XIA API tutorial!

The goal of this tutorial is to quickly show you how to build a complex application by using X-I-A API framework. 
This framework is microservice based in order to get a fast learning curve for developers and AI.

## How to use this tutorial

Each tutorial is ended by a series number like 01-02-03. The longer the series is, the more advanced topic is discussed.
It will be better to finish basic tutorial before going through advanced ones. Each tutorial has example code. 
Installation instruction could be found at tutorial/install.md.

## Prerequisites

Already finish the reading of [Tutorial API 01](https://github.com/X-I-A/xia-tutorial-api-01)

## Start with example

Please clone and deployed the example code (see [installation guide](tutorial/install.md) for instruction).

Or just visiting the already deployed [online version](https://xia-tutorial-api-01-01-srspyyjtqa-ew.a.run.app/order)

Only [models/purchase_order.py](models/purchase_order.py) has been modified to get the new data model work.

Here is a 40-second-video to show briefly how the new data model impacts the editor and api endpoints:

https://user-images.githubusercontent.com/49595269/212566125-f644dd46-3ba0-489d-a98f-c63f9b24cde5.mp4

## Data model
### Defining documents

A document is an independent information holder in the data model. Each document should be a subclass of Document object of xia-engine package.

You could find [Technical documentation](https://develop.x-i-a.com/docs/xia-engine/stable/_autosummary/xia_engine.document.Document.html#xia_engine.document.Document) of Document class to explore all options. 

### Adding fields

Fields are specified by adding field objects as class attributes to the document classes.

The basic field objects could be found in xia-fields package. Here is the [technical documentation](https://develop.x-i-a.com/docs/xia-fields/stable/index.html).

In order to create a field, just inheriting one of the pre-defined field types. It is also very simple to create a specific field class. Please check the following tutorials:

* Tutorial 01-01-01: Defining a specific simple field
* Tutorial 01-01-02: Understanding 5 data form of a field
* Tutorial 01-01-03: Defining a specific complex field

We are also developing xia-fields extensions for some widely used fields format. 

The pip package has the prefix `xia-fields-`, such as 
* [xia-fields-network](https://develop.x-i-a.com/docs/xia-fields-network/stable/index.html)

### Defining actions

A data model not only describes data but also performs the activities of the data, which is called actions.

Action is a method which meets two requirements:
* Defined in `_actions` class attributes of Document. `out` means the output type. 
If the `out` object is a subclass of `XiaFileMsg` of `xia-api` package, the output of API will be a file to be downloaded
```
class PurchaseOrder(Document):
    _actions = {"set_paid": {"out": XiaActionResult}}
```
* Having _acl parameter. _acl is used to control if the user has sufficient authorization to perform the action.
```
def set_paid(self, _acl=None):
    pass
```

### Defining embedded documents

An embedded document holds a subset information of a document. There are three ways to holds a subset information of a document:
`EmbeddedDocument`, `Reference`, `ExternalDocument`. To understand the design, please read the 
* Tutorial API 00-01: Descriptive Data Model

If you don't have time, a simplified rule is that when subset information cannot exist alone, `EmbeddedDocument` is the right way to go.

It is also possible to define action on embedded document level. It is not yet supported by editor, so you should call the url by using api endpoint.


